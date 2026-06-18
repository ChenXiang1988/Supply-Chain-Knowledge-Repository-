# 03Warehouse Management System

## 1. 文档信息

- 标题：03Warehouse Management System 目录说明
- 文档类型：工作区索引
- 版本：V1.1
- 日期：2026-06-18
- 作者：Martin
- 相关方：产品、研发、测试、仓内运营、OMS / TMS 对接、仓内主管

## 2. 目录定位

这个目录是 xzy 仓储管理系统（WMS）的业务文档工作区，不放实现代码，只放需求分析、Plan、原型和 PRD，用来沉淀 WMS 的业务边界、流程规则、系统边界和待确认项。

- 对人类来说，这里是查 WMS 现在在做什么、为什么这么做、下一步该做什么的入口。
- 对 Codex 来说，这里是进入当前 WMS 业务上下文的入口，编辑任何 WMS 业务文档前，先看这里和 `00Requirements/`。

## 3. 当前主线

| 主题 | 需求分析 | Plan | 当前状态 | 备注 |
|---|---|---|---|---|
| 售后到货入库 | `00Requirements/After-sales Receipt Requirements.md` | `01Plan/20260617_Plan_AfterSalesReceipt.md` | 已推进到 Plan | 关注人工到货签收、售后待匹配、质检入库和上架 |
| 出库拦截 | `00Requirements/Outbound Interception Requirements.md` | `01Plan/20260618_Plan_OutboundInterception.md` | 已推进到 Plan | 关注复核前、手工打包完成、交接前拦截和结果回传 |
| 拦截后返库上架 | `00Requirements/Intercept Return Putaway Requirements.md` | `01Plan/20260618_Plan_InterceptReturnPutaway.md` | 已推进到 Plan | 关注返库池、集货单、扫码绑定和上架拆单 |

## 4. 目录结构

- `00Requirements/`：需求分析文档，先在这里确认问题、范围、系统边界和待确认项
- `01Plan/`：Plan 方案，需求分析确认后再写
- `03PRD/`：PRD 文档，Plan 和原型都确认后再写，当前预留

## 5. 当前工作方式

1. 先看 `00Requirements/`，确认业务理解和系统边界。
2. 需求分析确认后，再写 `01Plan/`。
3. Plan 确认后，再出原型。
4. 原型确认后，再写 `03PRD/`。
5. 如果新增主题，先补需求分析，再按阶段推进，不要跳阶段。

## 6. WMS 文档规则

- 正常到货、售后到货、出库拦截、拦截后返库要分开写，不能混成一条链路。
- 如果是售后退回入库，WMS 只保留三张作业单据：`到货签收单`、`质检入库单`、`上架单`。
- 到货签收不形成库存数量，库存数量在质检入库时确认。
- 上架单只负责库位归位，不再改变数量。
- 没有 OMS 预通知时人工创建的到货签收单，只能进入售后待匹配，不允许转入正常到货流程。
- 出库拦截由上游系统触发，WMS 只负责接收、判断、阻断和回传，不主动创建拦截诉求。
- 拦截后返库上架只消费已打印的拦截结果，不再负责打印与模板配置。

## 7. 历史参考

| 文档 | 定位 |
|---|---|
| `01Plan/20260616_Plan_CBWH.md` | 早期返库上架方案，可作历史参考 |
| `01Plan/20260615_Plan_HW_step0.md` | 阶段 0 测试仓实施方案，可作历史参考 |

## 8. 当前关注主题

- `售后到货入库`
- `出库拦截`
- `拦截后返库上架`

如果新增一个 WMS 主题，先在 `00Requirements/` 新建或补齐需求分析，再按顺序推进到 Plan、原型和 PRD。
