# import base64
import os
import re
# import shutil
import stat
from email.utils import formatdate
from mimetypes import guess_type
from pathlib import Path
from urllib.parse import quote
from fastapi.responses import HTMLResponse,StreamingResponse
import aiofiles
from fastapi import Body, FastAPI, File, Path as F_Path, Request, UploadFile
import uvicorn


app = FastAPI()

@app.get("/")
def _():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <title>菜</title>
    </head>
    <body>
    <video width="906" height="510" controls preload autoplay>
      <source src="test.mp4" type="video/mp4">
      <object  width="320" height="240">
        <embed width="320" height="240" src="movie.swf">
      </object>
    </video>
    </body>
    </html>
    """


    return HTMLResponse(content=html)




@app.get("/{file_name}")
async def upload_file(request: Request, file_name: str = F_Path(..., description="文件名称（含后缀）")):
    """分片下载文件，支持断点续传"""
    # 检查文件是否存在
    abs_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(abs_path,file_name)
    if not os.path.exists(file_path):
        return {
            'code': 0,
            'error': '文件不存在'
        }
    # 获取文件的信息
    stat_result = os.stat(file_path)
    content_type, encoding = guess_type(file_path)
    content_type = content_type or 'application/octet-stream'
    # 读取文件的起始位置和终止位置
    range_str = request.headers.get('range', '')
    range_match = re.search(r'bytes=(\d+)-(\d+)', range_str, re.S) or re.search(r'bytes=(\d+)-', range_str, re.S)
    if range_match:
        start_bytes = int(range_match.group(1))
        end_bytes = int(range_match.group(2)) if range_match.lastindex == 2 else stat_result.st_size - 1
    else:
        start_bytes = 0
        end_bytes = stat_result.st_size - 1
    # 这里 content_length 表示剩余待传输的文件字节长度
    content_length = stat_result.st_size - start_bytes if stat.S_ISREG(stat_result.st_mode) else stat_result.st_size
    # 构建文件名称
    name, *suffix = file_name.rsplit('.', 1)
    suffix = f'.{suffix[0]}' if suffix else ''
    filename = quote(f'{name}{suffix}')  # 文件名编码，防止中文名报错
    # 打开文件从起始位置开始分片读取文件
    return StreamingResponse(
        file_iterator(file_path, start_bytes, 1024 * 1024 * 1),  # 每次读取 1M
        media_type=content_type,
        headers={
            'content-disposition': f'attachment; filename="{filename}"',
            'accept-ranges': 'bytes',
            'connection': 'keep-alive',
            'content-length': str(content_length),
            'content-range': f'bytes {start_bytes}-{end_bytes}/{stat_result.st_size}',
            'last-modified': formatdate(stat_result.st_mtime, usegmt=True),
        },
        status_code=206 if start_bytes > 0 else 200
    )

def file_iterator(file_path, offset, chunk_size):
    """
    文件生成器
    :param file_path: 文件绝对路径
    :param offset: 文件读取的起始位置
    :param chunk_size: 文件读取的块大小
    :return: yield
    """
    with open(file_path, 'rb') as f:
        f.seek(offset, os.SEEK_SET)
        while True:
            data = f.read(chunk_size)
            if data:
                yield data
            else:
                break




if __name__ == '__main__':
    uvicorn.run(app)

