# DynamicRender2.0
# 用途
用于将B站动态渲染成图片

```python
pip install dynamicrender

from dynamicrender.Renderer import BiliRender
from dynamicrender.DynamicChecker import Item


#item 为动态数据中的item

item = Item(**item)
img = await BiliRender(item).render()
```
