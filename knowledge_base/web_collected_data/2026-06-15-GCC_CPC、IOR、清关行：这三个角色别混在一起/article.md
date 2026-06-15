---
title: GCC/CPC、IOR、清关行：这三个角色别混在一起
author: 货代Agent
date: DarrenThinker
source_url: https://mp.weixin.qq.com/s/jIAA5xs20NnY3fd0fsCEoQ
capture_time: 2026-06-15 17:35:41
---

# GCC/CPC、IOR、清关行：这三个角色别混在一起

工厂给报告，进口商担责任，broker 负责把数据报进去

上一篇 CPSC eFiling 发出去后，评论区有几个问题很典型。

GCC 证书是不是买方基于生产商提供的测试报告签发的？如果通过货代 IOR 进口到美国，是不是由这个 IOR 签发 GCC？

如果我是卖家，从工厂采购产品，通过货代 Bond 进口到美国后进入海外仓再卖，那么工厂、卖家、清关行、IOR、eFiling 之间的关系到底怎么排？

这些问题如果只用一句话回答，很容易越说越乱。

因为大家把三件事混在一起了：**谁有测试资料，谁是证书责任方，谁在 entry 里提交数据。**

## 01先把一句话讲透

如果是进口到美国的 CPSC 管制消费品，证书责任通常落在美国进口商这一侧。

工厂可以提供测试报告、生产信息、型号、批次、实验室资料，也可以帮忙整理 CPC/GCC 草稿。

但清关时真正要经得起追问的是：**谁作为 importer/certifier 对这批货的合规负责？**

清关行或者快递报关团队做的是提交动作，不是替客户承担产品合规责任。

## 02原文里怎么说？

CPSC 的 GCC 页面里，对证书第 3 项的要求是：

“Identification of the domestic manufacturer or importer certifying compliance of the product.”

中文意思是：要写明对产品合规进行认证的美国境内制造商或进口商。

CPSC 对一般用途产品也说得很清楚：

“A manufacturer or importer must issue a General Certificate of Conformity.”

也就是说，GCC 不是“实验室报告本身”，而是制造商或进口商基于测试结果或合理测试计划作出的合规声明。

儿童产品 CPC 的逻辑也类似。CPSC 在 CPC FAQ 里提到，签发 CPC 的是 manufacturer or importer，并且证书要包含规定的七项信息。

## 03工厂到底扮演什么角色？

中国工厂最常见的角色，是资料提供方。

1. 提供测试报告。

2. 提供产品型号、SKU、批次、生产日期、生产地点。

3. 提供实验室信息和联系人。

4. 在客户要求下，帮助整理 CPC/GCC 模板。

但这不等于“工厂天然就是美国进口证书责任方”。

很多货代实操里会看到工厂拿出一份 GCC/CPC，上面写着工厂名字、实验室名字、产品型号。这个文件有没有用？有用，它可以作为资料来源。

但如果真正进口美国的是另一个 IOR，entry 上的 importer 又是另一家公司，那就要问一句：**这份证书里的 certifier，和这票货的进口责任链能不能解释得通？**

## 04卖家是不是一定要自己签？

不一定，要看卖家在美国进口链条里是什么身份。

如果卖家自己是美国 importer，或者用自己的主体做 IOR，那它通常就要把证书、测试报告、记录联系人这些东西管起来。

如果卖家只是境外卖家，使用货代或第三方 IOR 进口，那就进入了灰色但很现实的实操区：货代 IOR 愿不愿意作为进口商承担这批产品合规责任？卖家能不能把完整资料提供给 IOR？出了 CPSC 追问，谁能在美国响应？

这也是为什么未来很多“万能 IOR”会越来越难做。

过去可能只看商业发票、箱单、HTS、货值、收件人。以后涉及 CPSC 的产品，会多一层追问：**这票货的证书责任方到底是谁？**

## 05清关行负责什么？

清关行的核心角色，是把进口商提供的数据通过 entry 报给 CBP/CPSC。

CPSC eFiling FAQ 把两种方式讲得很清楚。

Full PGA Message Set: importer provides broker with the seven required product certificate data elements.

Reference PGA Message Set: importer pre-enters the product certificate data into the CPSC Product Registry and then provides their broker with Certificate Identifiers.

这里的关键词是 importer provides broker。

broker 不是凭空编证书，也不是看到客户说“我有报告”就自动替客户签字。

broker 要的是结构化数据：Product ID、Citation Codes、Manufacture Date、Manufacture Place、Product Test Date、Testing Laboratory、Point of Contact。

如果走 Product Registry，CPSC 还特别提醒：Registry 不会自动和 ACE 通信。

“does not communicate with CBP’s ACE system.”

所以进口商还是要把 Certifier ID、Product ID、Version ID 这三个 Certificate Identifiers 给 broker，broker 才能在 entry 里引用。

## 06那评论里的三方关系，怎么排才对？

| 角色 | 通常负责什么 | 最容易误解的地方 |
| --- | --- | --- |
| 工厂 | 测试报告、生产资料、型号批次 | 有报告不等于自动承担美国进口责任 |
| 卖家 | 组织资料、确定产品合规、对接 IOR | 不是 IOR 时，也不能完全甩手 |
| IOR | 进口责任、证书数据、记录响应 | 不能只收钱做名义进口商 |
| 清关行 | 按进口商资料提交 entry 和 PGA 数据 | 提交数据不等于替客户签证书 |

所以评论里的关系，可以这样理解：

1. 工厂提供测试报告和产品资料，这是证书的底层依据。

2. 卖家如果是品牌方或实际控制产品的人，要把资料组织好，不能只说“工厂有报告”。

3. IOR 如果作为进口商，就要能解释为什么它有资格为这票货承担进口和证书数据责任。

4. 清关行根据 IOR/进口商提供的数据做 entry 和 eFiling，不应该替客户创造不存在的合规关系。

## 07最危险的实操，不是资料缺，而是关系对不上

实务里真正麻烦的，往往不是“有没有测试报告”。

很多客户能拿出一堆 PDF：测试报告、CPC、GCC、Amazon 合规截图、供应商声明。

但一追问就乱了：

1. 报告上的型号和发票 SKU 对不上。

2. 证书上的 importer 和 entry 上的 IOR 不一致。

3. Point of Contact 写的是工厂业务员，但美国这边没人能响应。

4. 产品换了材料、批次、供应商，但还是沿用旧证书。

5. 货代 IOR 名义进口，但卖家不给完整资料，出了问题又说“这是你们清关的”。

这些才是后面容易卡住的地方。

## 08货代可以怎么跟客户说？

可以用这段话：

CPSC 的 CPC/GCC 不是单纯的实验室报告，也不是清关行替你填一张表。工厂可以提供测试报告和生产资料，进口商或美国境内制造商通常是证书责任方。清关行负责把进口商提供的证书数据通过 ACE/CPSC PGA message set 报进去。如果证书抬头、IOR、产品型号、测试报告、记录联系人之间对不上，后续被问到时就会很难解释。

再具体一点，可以让客户先确认五件事：

1. 这票货是否属于 CPSC 管制产品。

2. 需要 CPC 还是 GCC。

3. 谁是美国进口商或证书责任方。

4. 测试报告、型号、批次、证书数据是否能一一对应。

5. 谁把 Full PGA 数据或 Product Registry 的三个编号给 broker。

## 09最后的判断

这件事不能简单理解成“谁签个 GCC 就行”。

更准确的理解是：

**工厂提供证据，进口商承担证书责任，清关行提交数据，卖家要把这条链条组织起来。**

如果卖家、IOR、证书责任方、测试报告之间能闭环，这票货就比较稳。

如果只是拿一个工厂 PDF、借一个 IOR、让清关行临时填一填，那不是不能清，而是风险会越来越集中。

未来拼柜、快件、海外仓备货、平台卖家都会遇到这个问题。

不是所有货都要一对一绑定 IOR 才能走，但每一票受 CPSC 管制的货，都要能说清楚：**谁为这个产品在美国进口环节负责。**

**货代知识库**  
国际物流知识学习平台  
get.huodaiagent.com

参考资料：CPSC General Certificate of Conformity、CPSC Children's Product Certificate FAQ、CPSC eFiling FAQ、15 U.S.C. 2063、16 CFR Part 1110。本文为货代业务沟通参考，不替代美国进口商、报关行或专业律师意见。