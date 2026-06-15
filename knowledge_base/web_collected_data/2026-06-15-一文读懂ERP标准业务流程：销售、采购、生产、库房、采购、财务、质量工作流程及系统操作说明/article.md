---
title: 一文读懂ERP标准业务流程：销售、采购、生产、库房、采购、财务、质量工作流程及系统操作说明
author: 数智战略
date: Lisa
source_url: https://mp.weixin.qq.com/s/sGp62xonuDnsYEBjpcyCLQ
capture_time: 2026-06-15 17:36:28
---

# 对于企业来说，ERP 标准业务流程是打通销售、采购、生产、库房、财务全链路的核心骨架，规范流程不仅能减少错单、漏单，更能让成本核算、库存管理、财务对账精准高效。

---

## 1️⃣ 销售管理流程（SA）

**核心闭环**：合同→订单→发货→开票→收款/退货

![图片](images/img_001.png)

![图片](images/img_002.png)

![图片](images/img_003.png)

![图片](images/img_004.png)

```
客户签合同 → 存货/项目建档 → 录入+审核销售订单 → 生成发货通知单 → 销售出库 → 开票通知 → 应收挂账 → 收款核销  
└── 退货：红字退货单 → 红字发票 → 冲销收入/成本
```

**关键**：分普通/分期收款/直运3类业务，退货走红字冲销

---

## 2️⃣ 采购管理流程（PU）

**核心闭环**：计划→订单→到货→质检→入库→结算/暂估

![图片](images/img_005.png)

![图片](images/img_006.png)

![图片](images/img_007.png)

![图片](images/img_008.png)

![图片](images/img_009.png)

```
销售订单 → MRP运算 → 生成采购计划 → 录入+审核采购订单 → 到货报检 → 质检合格入库 → 采购结算/月末暂估  
└── 退货：红字入库单 → 红字发票 → 冲减应付/成本
```

**关键**：发票未到做暂估，次月自动红蓝回冲

---

## 3️⃣ 生产统计流程（MA）

**核心闭环**：订单→领料→生产→完工→入库→统计

![图片](images/img_010.png)

![图片](images/img_011.png)

```
```
总调下达生产订单 → 车间算料→填制领料单 → 材料出库 → 生产加工 → 完工通知 → 质检 → 产成品入库 → 工时/产量上报财务
```
```

**关键**：覆盖车体改装/机加/系统集成全生产环节

---

## 4️⃣ 库房业务流程（ST）

**核心闭环**：领用→入库→外协→备品/借还管理

![图片](images/img_012.png)

![图片](images/img_013.png)

![图片](images/img_014.png)

![图片](images/img_015.png)

![图片](images/img_016.png)

![图片](images/img_017.png)

![图片](images/img_018.png)

![图片](images/img_019.png)

```
材料领用：生产订单 → 算料领料 → 材料出库 → 成本归集  
产成品入库：完工→质检→入库→成本核算  
外协加工：半成品出库→外协加工→完工入库→费用挂账  
└── 备品/借还：0成本入库、调拨单管控
```

**关键**：外协厂设虚拟仓库，备品入库单价为0

---

## 5️⃣ 存货核算流程（IA）

**核心闭环**：单据→记账→成本→对账

![图片](images/img_020.png)

![图片](images/img_021.png)

![图片](images/img_022.png)

![图片](images/img_023.png)

```
库房出入库单据 → 存货核算记账 → 采购/销售/领用成本计算 → 产成品成本分配 → 月末库存/总账对账  
└── 暂估：月末入库未结算→暂估记账→次月发票到→红蓝回冲
```

**关键**：全模块自动取数，月末必须对账

---

## 6️⃣ 成本核算流程（CA）

**核心闭环**：费用归集→分配→成本计算→结转

![图片](images/img_024.png)

```
材料费用（存货）+人工/制造费用（总账） → 成本模块取数 → 完工/在产品分配 → 产成品成本计算 → 结转生产成本
```

**关键**：月末统一核算，料工费全归集

---

## 7️⃣ 财务核算流程（AR/AP/GL）

**核心闭环**：应收→应付→总账结账

![图片](images/img_025.png)

![图片](images/img_026.png)

![图片](images/img_027.png)

```
应收：销售开票→审核挂账→收款核销→制单  
应付：采购发票→审核挂账→付款核销→制单  
总账：凭证制单→审核→记账→生成报表→月末结账
```

**关键**：业务单据自动生成凭证，支持逆向操作

---

## 8️⃣ 质量管理流程（QM）

**核心闭环**：报检→质检→入库/退货

![图片](images/img_028.png)

![图片](images/img_029.png)

![图片](images/img_030.png)

![图片](images/img_031.png)

```
采购检验：到货→报检→质检→合格入库/不合格退货  
成品检验：生产完工→报检→质检→合格入库/不良品处理
```

**关键**：不合格品走分拣/退货流程，闭环管控

---

## 9️⃣ 集中结算流程（FD）

**核心闭环**：明细→汇总→确认→制单

```
收款单位填结算明细表 → 审核 → 结算中心汇总审核 → 付款单位确认 → 财务制单结账
```

**关键**：统一结算，三方确认，数据可追溯

![图片](images/img_032.png)

[数字化社群，欢迎各位共同学习](https://mp.weixin.qq.com/s?__biz=MzkyNTUxMDUxNQ==&mid=2247504547&idx=1&sn=59d747697afd116e09f432ef9f29ea65&scene=21#wechat_redirect)

[集团AI应用蓝图规划方案：从零散试点到价值规模化](https://mp.weixin.qq.com/s?__biz=MzkyNTUxMDUxNQ==&mid=2247507602&idx=1&sn=212bcb2f33bcb49196d052ef8e01dbd5&scene=21#wechat_redirect)

[信息部总监2026年一季度数字化转型工作总结及二季度计划](https://mp.weixin.qq.com/s?__biz=MzkyNTUxMDUxNQ==&mid=2247509495&idx=1&sn=d3c9fce182c1555b24dce3be97735531&scene=21#wechat_redirect)

[IBM化工行业数字化转型：从战略到落地的全景方](https://mp.weixin.qq.com/s?__biz=MzkyNTUxMDUxNQ==&mid=2247509472&idx=1&sn=1c2b3453a4f3f6c30f05f08439562d86&scene=21#wechat_redirect)

[基于AI Agent的智能工厂规划方案：排程从4小时缩至15分钟](https://mp.weixin.qq.com/s?__biz=MzkyNTUxMDUxNQ==&mid=2247507949&idx=1&sn=ed2220267e3d1af3a23cb1542ef9c193&scene=21#wechat_redirect)

[集团AI应用蓝图规划方案：从零散试点到价值规模化](https://mp.weixin.qq.com/s?__biz=MzkyNTUxMDUxNQ==&mid=2247507602&idx=1&sn=212bcb2f33bcb49196d052ef8e01dbd5&scene=21#wechat_redirect)

[AI Agent的核心架构与能力模块：感知、规划与行动的协同机制](https://mp.weixin.qq.com/s?__biz=MzkyNTUxMDUxNQ==&mid=2247500776&idx=1&sn=7d9e79bee9a3de7eb08c44e7e5ed20da&scene=21#wechat_redirect)

[AI智能体设计全指南：从提示词高手到Agent架构师](https://mp.weixin.qq.com/s?__biz=MzkyNTUxMDUxNQ==&mid=2247508093&idx=1&sn=9c050a4f7e7e8aaf5a89e0a7f6d99faa&scene=21#wechat_redirect)

[2026 灯塔工厂全景报告：标准、申报与价值全解](https://mp.weixin.qq.com/s?__biz=MzkyNTUxMDUxNQ==&mid=2247509664&idx=1&sn=fc436f223352de3d5b889f82c93154cd&scene=21#wechat_redirect)

[企业数字化转型IT架构蓝图设计方法论](https://mp.weixin.qq.com/s?__biz=MzkyNTUxMDUxNQ==&mid=2247509641&idx=1&sn=04dad77912cfdf0c3bd3be81f0170baa&scene=21#wechat_redirect)

[IBM化工行业数字化转型：从战略到落地的全景方法](https://mp.weixin.qq.com/s?__biz=MzkyNTUxMDUxNQ==&mid=2247509472&idx=1&sn=1c2b3453a4f3f6c30f05f08439562d86&scene=21#wechat_redirect)

[从PLM到MOM：集团制造数字化转型全链路方案](https://mp.weixin.qq.com/s?__biz=MzkyNTUxMDUxNQ==&mid=2247509392&idx=1&sn=9544ae5cb6475186f8260dc2a4a2aab0&scene=21#wechat_redirect)

[IBM企业IT治理蓝图和数字化转型战略](https://mp.weixin.qq.com/s?__biz=MzkyNTUxMDUxNQ==&mid=2247509003&idx=1&sn=4589aa27e8a5e4446b5d888367f2bd86&scene=21#wechat_redirect)

[网络安全实战攻防演练及网络安全意识培训](https://mp.weixin.qq.com/s?__biz=MzkyNTUxMDUxNQ==&mid=2247507764&idx=1&sn=bf900377b7c5572227ceb9aa19fafaed&scene=21#wechat_redirect)

[一文读懂从数据资产入表到数据金融化，到底怎么做？](https://mp.weixin.qq.com/s?__biz=MzkyNTUxMDUxNQ==&mid=2247507985&idx=1&sn=ca39a8d1cba95d76ce026bb6e7a25513&scene=21#wechat_redirect)

[埃森哲智能工厂顶层规划方法论：数字化工厂规划架构与实践](https://mp.weixin.qq.com/s?__biz=MzkyNTUxMDUxNQ==&mid=2247507050&idx=1&sn=974172a41b4db98a8b07446a287485a4&scene=21#wechat_redirect)

[埃森哲智能制造与卓越运营方法领](https://mp.weixin.qq.com/s?__biz=MzkyNTUxMDUxNQ==&mid=2247502527&idx=1&sn=9cb79ae546d83f0e05f355240169b970&scene=21#wechat_redirect)

[IBM信息化咨询规划方法论](https://mp.weixin.qq.com/s?__biz=MzkyNTUxMDUxNQ==&mid=2247505307&idx=1&sn=1c95d42472a9bfdc2308ce8971dc4ac4&scene=21#wechat_redirect)

[华为数据治理三阶十八步法](https://mp.weixin.qq.com/s?__biz=MzkyNTUxMDUxNQ==&mid=2247507725&idx=1&sn=4b971c7a420a5d60ec239a4c2d16e764&scene=21#wechat_redirect)

[德勤企业IT蓝图规划：构建战略对齐的数字化转型框架](https://mp.weixin.qq.com/s?__biz=MzkyNTUxMDUxNQ==&mid=2247505216&idx=1&sn=5c7e8a4fae8a503ac659ce265ca23aa5&scene=21#wechat_redirect)