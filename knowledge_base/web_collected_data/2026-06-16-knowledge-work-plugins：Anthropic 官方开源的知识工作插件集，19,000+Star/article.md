---
title: knowledge-work-plugins：Anthropic 官方开源的知识工作插件集，19,000+Star
author: 赛博虾酱
date: 新世界圆圆圆
source_url: https://mp.weixin.qq.com/s/aSiMQfpvQc7Qup1aVQwJUg
capture_time: 2026-06-16 18:37:21
---

 

> GitHub: https://github.com/anthropics/knowledge-work-plugins  
> 协议：Apache 2.0  
> 开发者：Anthropic 官方  
> 产品集成：Claude Cowork + Claude Code

## 一句话介绍

**Anthropic 官方开源的一套知识工作插件——给 Claude 装上销售、客服、产品、法务、金融、数据、营销、HR、工程等岗位的专业技能和工具连接。** 每个插件都是纯 markdown + JSON，不需写代码，装完 Claude 就懂那个岗位怎么做活。

---

## 先理解产品背景

Anthropic 的产品定位在 2026 年有一条清晰的分界线：

* • **Claude Code** 面向开发者——在终端里帮你写代码
* • **Claude Cowork** 面向知识工作者——在浏览器里帮你做文档、处理信息、跨工具协作

这个仓库就是 Cowork 和 Claude Code 的"APP Store"。它不帮你写代码。它帮你做知识工作。

---

## 20 个插件，覆盖企业岗位

仓库里有 20 个插件目录。每个目录对应一个角色或职能：

| 插件 | 定位 | 连接的工具 |
| --- | --- | --- |
| **sales** | 潜在客户研究、电话准备、管道审查、竞争情报 | Slack, HubSpot, Close, Clay, ZoomInfo, Fireflies |
| **customer-support** | 工单分流、客户回复、升级包装、知识库 | Slack, Intercom, Guru, Jira, Notion |
| **product-management** | 需求文档、路线图、用户研究、竞品追踪 | Slack, Linear, Asana, Monday, Jira, Figma, Amplitude, Pendo, Intercom |
| **marketing** | 内容草稿、营销计划、品牌调性、竞品简报 | Slack, Canva, Figma, HubSpot, Amplitude, Ahrefs, SimilarWeb, Klaviyo |
| **finance** | 日记账、对账、财务报表、差异分析、闭环管理 | Snowflake, Databricks, BigQuery, Slack, Microsoft 365 |
| **data** | SQL 查询、数据可视化、统计分析、仪表板构建 | Snowflake, Databricks, BigQuery, Definite, Hex, Amplitude |
| **legal** | 合同审核、NDA 审查、合规导航、风险分析 | Slack, Box, Egnyte, Jira, Microsoft 365 |
| **engineering** | 技术文档、代码审查、架构设计 | 工程工具链 |
| **design** | 设计系统、组件库、品牌一致性 | Figma 等设计工具 |
| **human-resources** | 招聘、入职、绩效、员工手册 | HRIS 系统 |
| **operations** | 流程自动化、SOP、运维监控 | 运营工具链 |
| **enterprise-search** | 跨工具全量搜索 | Slack, Notion, Guru, Jira, Asana, Microsoft 365 |
| **bio-research** | 文献搜索、基因组分析、靶点筛选 | PubMed, BioRender, ChEMBL, Open Targets, Benchling |
| **productivity** | 任务、日历、日常流程、个人信息管理 | Slack, Notion, Asana, Linear, Jira, Microsoft 365 |
| **cowork-plugin-management** | 创建新插件、自定义现有插件 | — |
| **small-business** | 小企业全方位管理 | 小企业工具栈 |
| **pdf-viewer** | PDF 审阅和标注 | PDF 处理 |
| **partner-built** | 合作伙伴构建的插件 | 合作伙伴工具 |

算下来覆盖了企业里绝大多数知识工作者的岗位。从 CRM 打单到 SQL 取数、从用户研究到合同审查。

---

## 一个插件里有什么

每个插件目录遵循同样的结构：

```
plugin-name/  
├── .claude-plugin/plugin.json   # 清单文件（插件名、描述、依赖）  
├── .mcp.json                    # 工具连接（MCP server 配置）  
├── commands/                    # 用户调用的 slash command  
└── skills/                      # 自动触发的领域知识
```

全是 markdown 和 JSON。没有代码。没有基础设施。没有构建步骤。

* • **Skills** 编码了领域专业知识、最佳实践、分步工作流
* • **Commands** 是用户主动调用的动作（`/sales:call-prep`）
* • **Connectors** 通过 MCP server 连接外部工具

一个典型的使用流程：

```
用户 > 下周要和 Acme Corp 的 CTO 通电话，帮我准备一下  
  
Claude Cowork / Code（装了 sales 插件）>  
    1. 连接 HubSpot 读 Acme Corp 的公司概况和最近的销售活动  
    2. 连接到 LinkedIn 了解 CTO 的背景和最近动态  
    3. 搜索内部 Slack 频道里上一次跟 Acme Corp 相关的讨论  
    4. 准备一份通话摘要和目标（基于 sales 插件的 call-prep skill）  
    5. 生成可能的提问清单（基于 sales 插件的 discovery skill）  
    6. 可选：自动生成日历邀请
```

不需要人类告诉 Claude"先去 A 系统查客户信息、再去 B 系统看会议记录、再按什么模板生成摘要"。skill 文件里已经编码了这个流程。

---

## Anthropic 的产品战略

这个仓库反映了 Anthropic 在 2026 年的一个关键战略转折：**从"一个聊天机器人"变成了"一个组织级工具"。**

具体的特征：

**1. 插件是组织级别的资产。** 不是"每个员工自己去配 Claude"。是管理员部署一个插件到全公司。所有人开的 Claude 都有相同的 sales、marketing、data 技能。输出质量和风格统一。

**2. 定制化不是写代码。** 所有的插件内容都是 markdown。修改一个 skill 的工作流、替换一个 MCP 连接、添加公司的内部术语——全部通过编辑几个 .md 文件完成。非技术角色的经理可以自己改。

**3. 生态押在 MCP 上。** 每个插件的 Connectors 都走 MCP server。目前支持的连接器已经覆盖了大多数 SaaS 企业工具——Slack, Notion, HubSpot, Salesforce, Jira, Figma, Snowflake, BigQuery, Canva。这是用 MCP 协议在画企业的集成地图。

---

## 怎么装

**Cowork 用户：** 从 `claude.com/plugins` 安装

**Claude Code 用户：**

```
# 添加插件市场  
claude plugin marketplace add anthropics/knowledge-work-plugins  
  
# 安装具体插件  
claude plugin install sales@knowledge-work-plugins
```

装完后 skill 会自动触发，slash command 在对话中可用：

```
/sales:call-prep       # 准备销售电话  
/data:write-query      # 写 SQL 查询  
/finance:reconciliation # 对账  
/product-management:write-spec  # 写产品规格
```

---

## 适用场景

**企业级 Claude 部署。** 你需要全员用 Claude 但又想让所有人的输出风格和方法论一致。一人装一个插件，全公司统一。

**特定岗位的 AI 加速。** 销售团队不想自己学怎么写 prompt。装了 sales 插件后，Claude 直接在 CRM 上下文中帮销售写 outreach email、准备通话摘要。销售不需要知道什么是 skill 或 MCP。

**知识工作流的自动化。** 一个典型的"知识岗位 AI 团队"场景：

* • Sales 用 sales 插件预热客户
* • PM 用 product-management 插件写 PRD
* • 工程用 engineering 插件做设计评审
* • PM 和销售都用 enterprise-search 查公司决策历史

所有操作都在 Claude 里完成，所有插件共享同一个知识体系。

---

## 和 Claude Code Plugins 的区别

Claude Code Plugins 面向开发场景——`feature-dev`、`pr-review-toolkit`、`security-guidance`。

Knowledge Work Plugins 面向非开发场景——`sales`、`finance`、`legal`、`data`。

两者的插件体系是一样的（都是 markdown + JSON + skills + commands + MCP）。只是面向的用户不同。

**两者也可以叠加使用。** 工程师开着 engineering 插件写代码，同时也开着 productivity 插件管理日程。

---

## 总结

这个仓库的意义不在"19,000 Star"。意义在它是 Anthropic 从"to-C 聊天产品"转向"to-B 企业平台"的关键一步。

20 个岗位插件覆盖企业知识工作的主要职能部门。所有插件都是文件级的 markdown/JSON——非技术人员能定制、管理员能部署、开发者能做版本管理。

如果你公司的知识工作者已经开始用 Claude，这个仓库里的插件是让他们从"手动写 prompt"到"Claude 自动用工具"的最后一块拼图。

点击下方名片「关注我们」第一时间收到推送

 