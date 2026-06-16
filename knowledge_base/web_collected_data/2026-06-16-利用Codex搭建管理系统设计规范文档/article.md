---
title: 利用Codex搭建管理系统设计规范文档
author: 图层没命名
date: Erivorn
source_url: https://mp.weixin.qq.com/s/FCIZInNHhti1fzwrulshHw
capture_time: 2026-06-16 18:36:32
---

* 参考成熟设计规范，生成设计规范md文件

具体指令也是初步借鉴他人的，可根据需求自行调整

![图片](images/img_001.png)

* 使用生成的md文件进行设计规范搭建

后续设计规范内容的呈现很大程度上取决于md文件的详尽程度

![图片](images/img_002.png)

* 初次生成，还是有不少问题

布局错乱，图表重复，icon出错

![图片](images/img_003.png)

![图片](images/img_004.png)

* 继续输出指令让Codex进行调整

输出结果还是需要人工排查，输入指令进一步调整

![图片](images/img_005.png)

![图片](images/img_006.png)

![图片](images/img_007.png)

* 最后

最后的结果也算是出来了，但icon还是有些问题（估计写入svg的bug）

![图片](images/img_008.png)

变量库也完成了

![图片](images/img_009.png)

按钮组件的变体也有实现，但自动布局还是需要修补

![图片](images/img_010.png)

* 总结

虽说可以直接用公开的一些更完整的组件库（调整改动不大）。但这也是一种新的设计规范搭建方式（有些调整还是离不开人工，命名方式也需提前设定），后续也可以直接根据参考图/网页链接进行二次创作。