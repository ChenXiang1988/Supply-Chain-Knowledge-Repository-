# 泓湖3PL平台

## 项目简介

泓湖3PL平台是一套面向第三方物流企业的完整服务体系，涵盖仓储管理、订单管理、库存管理、客户协同、经营分析等核心能力。当前处于蓝图设计阶段，第一期试点范围已冻结。

本工作区存放项目的所有文档，包括蓝图设计、场景需求、流程设计、数据设计等。无论你是项目经理、产品经理、架构师、研发、测试还是实施同学，都能在这里找到你需要的文档。

---

## 快速入口

### 项目经理 (Project Manager)
- [试点范围](./blueprint/2026-06-20-hh-pilot-scope.md) - 了解第一期要做哪些功能
- [场景清单](./scenarios/2026-06-18-3pl-scenario-list.md) - 查看所有业务场景及优先级
- [实现路径](./blueprint/2026-06-18-3pl-blueprint-implementation-path.md) - 了解从设计到落地的步骤

### 产品经理 (Product Manager)
- [用户画像](./scenarios/2026-06-18-3pl-user-personas.md) - 了解系统使用者
- [场景需求](./scenarios/) - S-01 到 S-07 详细需求文档
- [权限矩阵](./scenarios/2026-06-20-3pl-permission-matrix.md) - 功能权限设计

### 架构师 (Architect)
- [平台蓝图](./blueprint/2026-06-17-global-3pl-platform-blueprint-design.md) - 总体架构设计
- [领域模型](./blueprint/2026-06-17-3pl-domain-model.md) - 核心数据模型
- [系统终端](./scenarios/2026-06-20-3pl-system-terminals.md) - 产品端划分

### 研发 (Developer)
- [主干流程V2](./blueprint/2026-06-20-3pl-core-flow-v2.md) - 核心业务流程
- [端侧流程](./flows/) - 各端详细流程设计
- [单据结构](./data-design/2026-06-20-3pl-document-structure.md) - 数据结构设计
- [API规范](./api/README.md) - API文档编写规范（待补充）

### 测试 (Tester)
- [场景需求](./scenarios/) - 测试依据
- [流程设计](./flows/) - 流程测试用例来源
- [测试规范](./test/README.md) - 测试文档编写规范（待补充）

### 实施 (Implementation)
- [试点范围](./blueprint/2026-06-20-hh-pilot-scope.md) - 实施范围
- [仓型配置](./blueprint/2026-06-17-3pl-country-warehouse-config.md) - 配置规范
- [实施规范](./implementation/README.md) - 实施文档编写规范（待补充）

---

## 文档地图

### 📐 蓝图设计 ([blueprint/](./blueprint/))
顶层设计文档，定义平台的目标、架构、能力和实施路径。

| 文档 | 简介 |
|------|------|
| [全球3PL平台蓝图总纲](./blueprint/2026-06-17-global-3pl-platform-blueprint-design.md) | 平台目标、设计原则、总体架构 |
| [3PL业务能力树](./blueprint/2026-06-17-3pl-capability-tree.md) | 分层展示平台核心能力 |
| [领域模型设计](./blueprint/2026-06-17-3pl-domain-model.md) | 核心数据模型与对象定义 |
| [RBAC权限矩阵](./blueprint/2026-06-17-3pl-rbac-matrix.md) | 角色权限设计（旧版） |
| [主流程泳道图](./blueprint/2026-06-17-3pl-core-flow-swimlanes.md) | 主流程设计（已被V2替代，保留参考） |
| [国家/仓型配置规范](./blueprint/2026-06-17-3pl-country-warehouse-config.md) | 配置化设计，支持快速复制 |
| [蓝图实现路径](./blueprint/2026-06-18-3pl-blueprint-implementation-path.md) | 从设计到落地的实施步骤 |
| [行业参考案例](./blueprint/2026-06-18-3pl-reference-cases.md) | SCOR、SAP EWM、Oracle等参考 |
| [泓湖试点范围](./blueprint/2026-06-20-hh-pilot-scope.md) | 第一期试点范围（已冻结） |
| [试点主干流程V2](./blueprint/2026-06-20-3pl-core-flow-v2.md) | 泓湖试点主干流程（当前有效） |

### 📋 场景需求 ([scenarios/](./scenarios/))
详细的需求文档，描述每个业务场景的功能要求。

| 文档 | 简介 |
|------|------|
| [场景清单](./scenarios/2026-06-18-3pl-scenario-list.md) | 12个业务场景列表及优先级 |
| [用户画像](./scenarios/2026-06-18-3pl-user-personas.md) | 7层用户角色及职责定义 |
| [系统约束](./scenarios/2026-06-18-3pl-system-constraints.md) | 平台边界与设计约束 |
| [权限矩阵设计](./scenarios/2026-06-20-3pl-permission-matrix.md) | 按功能模块定义的权限矩阵 |
| [产品端划分](./scenarios/2026-06-20-3pl-system-terminals.md) | 6个产品端的功能清单 |
| [S-01 客户接入](./scenarios/2026-06-20-3pl-s01-customer-onboarding.md) | 客户入驻与账号开通流程 |
| [S-02 主数据初始化](./scenarios/2026-06-20-3pl-s02-master-data.md) | 仓库结构配置与SKU注册 |
| [S-03 入库预约](./scenarios/2026-06-20-3pl-s03-appointment.md) | 预约提交流程 |
| [S-04 收货上架](./scenarios/2026-06-20-3pl-s04-receiving.md) | 仓内入库执行流程 |
| [S-05 库存查询](./scenarios/2026-06-20-3pl-s05-inventory.md) | 库存可视化与查询功能 |
| [S-06 出库下单](./scenarios/2026-06-20-3pl-s06-order-fulfillment.md) | 客户下单与库存承诺 |
| [S-07 拣货发运](./scenarios/2026-06-20-3pl-s07-picking-shipping.md) | 仓内出库执行流程 |

### 🔄 流程设计 ([flows/](./flows/))
各端侧的系统流程设计，包含详细的Mermaid流程图。

| 文档 | 简介 |
|------|------|
| [Web管理后台-订单处理](./flows/flow-01-web-order-processing.md) | 订单处理全流程 |
| [PDA移动作业-拣货](./flows/flow-02-pda-picking.md) | 拣货作业流程（V2多人协同） |
| [客户门户-自助下单](./flows/flow-03-portal-order.md) | 客户自助下单流程 |
| [开放平台API-订单同步](./flows/flow-04-api-order-sync.md) | API订单同步流程 |
| [数据看板-BI分析](./flows/flow-05-bi-dashboard.md) | 数据流与展示流程 |
| [退货处理-RMA管理](./flows/flow-06-return-rmma.md) | RMA全生命周期流程 |

### 🗄️ 数据设计 ([data-design/](./data-design/))
数据结构与单据设计文档。

| 文档 | 简介 |
|------|------|
| [单据结构设计](./data-design/2026-06-20-3pl-document-structure.md) | 14个核心单据及状态流转 |

### 🔌 API文档 ([api/](./api/))
接口文档（规划中，待补充）

### 🧪 测试文档 ([test/](./test/))
测试用例、测试计划等（规划中，待补充）

### 🚀 实施文档 ([implementation/](./implementation/))
实施指南、配置手册等（规划中，待补充）

---

## 阅读顺序建议

### 第一次了解项目？
1. 本项目简介（本README）
2. [平台蓝图总纲](./blueprint/2026-06-17-global-3pl-platform-blueprint-design.md)
3. [业务能力树](./blueprint/2026-06-17-3pl-capability-tree.md)
4. [试点范围](./blueprint/2026-06-20-hh-pilot-scope.md)

### 深入业务设计？
1. [用户画像](./scenarios/2026-06-18-3pl-user-personas.md)
2. [场景清单](./scenarios/2026-06-18-3pl-scenario-list.md)
3. [S-01至S-07场景需求](./scenarios/)

### 准备实施？
1. [试点范围](./blueprint/2026-06-20-hh-pilot-scope.md)
2. [主干流程V2](./blueprint/2026-06-20-3pl-core-flow-v2.md)
3. [各端流程设计](./flows/)
4. [单据结构设计](./data-design/2026-06-20-3pl-document-structure.md)

---

## 文档命名规范

为了保持文档的一致性和可追溯性，请遵循以下命名规范：

- **蓝图文档**: `YYYY-MM-DD-3pl-<主题>.md`
  - 示例: `2026-06-20-hh-pilot-scope.md`

- **场景文档**: `YYYY-MM-DD-3pl-s<NN>-<场景名称>.md`
  - 示例: `2026-06-20-3pl-s01-customer-onboarding.md`

- **流程文档**: `flow-<NN>-<流程名称>.md`
  - 示例: `flow-01-web-order-processing.md`

- **数据设计文档**: `YYYY-MM-DD-3pl-<主题>.md`
  - 示例: `2026-06-20-3pl-document-structure.md`

---

## 项目状态

- **当前阶段**: 蓝图设计完成，场景需求编写中
- **文档状态**: 草案 (V0.1)
- **试点范围**: 已冻结（2026-06-20）
- **最后更新**: 2026-06-20

---

## 如何贡献

如果你需要添加或修改文档：

1. 遵循上述命名规范
2. 在对应的目录下创建/编辑文档
3. 更新该目录的README.md（如果有）
4. 如涉及重大变更，请更新本文档的"项目状态"部分

---

**让每个人都能快速找到所需的文档 🚀**
