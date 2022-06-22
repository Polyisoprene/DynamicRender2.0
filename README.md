# DynamicRender2.0
# 用途
用于将B站动态渲染成图片

```python
pip install dynamicrender

from dynamicrender.Renderer import BiliRender

#item 为动态数据中的item


img = await BiliRender(item).render()
```
