AGENTS.md：给 AI 编程Agent看的“项目 README”

当越来越多团队把 Cursor、Aider、VS Code 的 AI 插件、Devin、Windsurf 等 coding agent 引入日常开发后，一个现实问题很快浮现：Agent需要稳定、明确、可机器读取的项目上下文。但我们常见的 README.md 往往是“写给人看的”——既要介绍产品、又要写贡献指南、还要塞进构建/测试/格式化命令，最后变得又长又杂；而Agent在这种文档里找关键操作步骤，很容易遗漏、误解或走偏。

AGENTS.md 正是为此而生：它提供了一个简单、开放的约定——在仓库里放一个名为 AGENTS.md 的 Markdown 文件，专门用来写“给 AI 编程Agent看的项目说明”。你可以把它理解为：



给 coding agents 的 README：只讲上下文、命令、规则、路径、约束；不做营销、不写长篇人类叙事。

项目主页：https://agents.md/



它解决什么问题？





把“人类 README”从指令泥潭里解放出来





README.md 需要面向新人、人类贡献者、产品用户；



Agent更需要可执行的细节：如何安装依赖、跑测试、生成代码后要改哪里、CI 失败怎么看。



给Agent一个确定、可预期的“入口文件”





与其让Agent在仓库里猜“是不是 CONTRIBUTING.md”、“是不是 docs/dev.md”，不如约定：就看 AGENTS.md。



在大型仓库/Monorepo 里支持“就近生效”





AGENTS.md 支持在子目录里放嵌套文件；



Agent应读取“离当前文件最近的那个 AGENTS.md”，从而让不同子项目拥有自己的构建命令与规范。



核心设计：简单、开放、分层

1) 开放格式：就是 Markdown

AGENTS.md 不引入专有 DSL，也不强制字段结构——你写的就是标准 Markdown。这意味着：





人和机器都能读；



现有文档体系不需要大改；



你可以按团队习惯持续演进。

2) 分层/优先级：离得越近越有效

在 Monorepo 或多模块项目中，你可以这样组织：





/AGENTS.md（全局约束：通用命令、通用规范）



/packages/foo/AGENTS.md（Foo 子项目：自己的 dev/test/build 方式）

并遵循优先级原则：





最接近目标文件/目录的 AGENTS.md 优先级最高；



用户在对话框里手动输入的指令优先级更高（即“聊天提示”压过文档）。

3) 广泛兼容：面向多种 agent 工具

项目主页列出的兼容对象包括（但不限于）：Cursor、Aider、VS Code、Devin、Windsurf 等主流 AI 编程Agent/IDE 工具链。



快速开始：3 分钟把Agent“带上路”

AGENTS.md 不需要安装任何软件：





在仓库根目录创建文件：AGENTS.md



把Agent真正需要的内容写进去（命令、路径、规则、边界条件）

一个足够实用的起步模板如下：

## Setup commands
- Install deps: `pnpm install`
- Start dev server: `pnpm dev`
- Run tests: `pnpm test`

## Code style
- TypeScript strict mode
- Single quotes, no semicolons

建议你在模板基础上继续补齐这几类高价值信息（能显著降低Agent“瞎猜”的概率）：





项目结构地图：关键目录、核心模块、入口文件



CI/测试矩阵：单测/集成测命令、覆盖范围、耗时提示



变更策略：改动某模块必须同步更新哪些文件、哪些 API 不能破坏



生成代码后的校验：lint/format/test 的最小闭环



安全与权限边界：不可触碰的密钥/生产配置、危险操作禁令



AGENTS.md 里该写什么？有“必填题/题目”吗？

先说结论：AGENTS.md 没有任何强制字段，也不存在官方规定的“必填题/固定题目”。它只是约定了一个文件名和承载格式（Markdown），内容完全由你决定。

为了让 Agent 的行为更稳定、可控，建议把内容写成“可执行的操作手册”，优先覆盖这些信息：





项目概览（面向 Agent）





这个仓库/子项目是做什么的、主要语言/框架是什么



哪些目录是核心，哪些是生成物/不要改



环境与依赖





Node/Python/Go 等版本要求



包管理器选择（pnpm/yarn/npm），以及锁文件要求



常用命令（最重要）





安装依赖：pnpm install



本地开发：pnpm dev



测试与覆盖：pnpm test / pnpm test --filter ...



构建与产物位置：pnpm build，build 输出目录



代码规范与约束





lint/format 规则与命令（例如 pnpm lint、pnpm fmt）



提交前必须通过哪些检查



生成代码时要遵守的风格要点（缩进、引号、文件命名等）



仓库规则（避免踩坑）





不要改动的文件/目录（例如 dist/、vendor/、package-lock.json）



变更某模块必须同步更新的地方（例如 API 变更要更新 OpenAPI/文档/测试）



常见失败与排查（例如 CI 某个 job 的入口脚本）



分层写法建议（适用于 Monorepo）





根目录 AGENTS.md 写全局通用规则



子目录 AGENTS.md 写该子项目的命令/路径/特殊约束



这样 Agent 在改某个子项目时能拿到“就近且准确”的指令

如果你希望更“像规范文档”一点，也可以用统一标题来组织（不是强制）：





## Purpose / ## 项目定位



## Setup / ## 安装与启动



## Test & CI / ## 测试与 CI



## Code Style / ## 代码规范



## Do & Don't / ## 必做与禁忌



与 README / CONTRIBUTING 的关系：不是替代，而是分工

一个常见误区是“再来一个文档会不会更乱？”——AGENTS.md 的思路恰恰相反：用明确分工降低整体混乱。





README.md：面向人类的项目介绍、使用方式、愿景、链接、截图



CONTRIBUTING.md：面向人类贡献者的流程、规范、PR 要求



AGENTS.md：面向 AI Agent的可执行上下文（命令、路径、规则、限制）

你可以把它理解成：把“可执行真相”集中到一个确定位置。



在具体工具里怎么接入？（示例）

AGENTS.md 是“约定优于配置”的思路，但部分工具也提供显式配置入口。项目主页给了两个例子：

Aider

在 .aider.conf.yml 中添加：

read: AGENTS.md

Gemini CLI

在 .gemini/settings.json 中配置：

{ "context": { "fileName": "AGENTS.md" }, }



常见问题（FAQ）

Q1：AGENTS.md 有强制字段或规范吗？

没有。它不强制 schema，完全自由格式（Markdown）。

Q2：如果根目录和子目录都有 AGENTS.md，会读哪个？

读离当前文件最近的那个，它优先级最高。

Q3：我现在用的是 AGENT.md（少了个 S）怎么办？

项目主页给了一个兼容迁移思路：可以重命名并用符号链接保留旧名字：

mv AGENT.md AGENTS.md && ln -s AGENTS.md AGENT.md

Q4：这个项目由谁维护？

项目由 Agentic AI Foundation（隶属于 Linux Foundation）管理，并以生态共建方式演进（主页提到 OpenAI、Google、Cursor 等参与者）。



什么时候你会真正“需要”AGENTS.md？

如果你符合下面任意一条，AGENTS.md 往往立刻能提升Agent产出质量：





仓库是 Monorepo，不同子项目命令/规范差异明显



项目构建步骤复杂，Agent经常跑错命令或漏掉关键步骤



团队有明确代码风格/目录约束，但Agent生成代码经常不合规



CI 规则多、脚本多，新同事和Agent都容易“踩坑”



小结

AGENTS.md 的价值不在于“又发明一个新文档”，而在于它把一个关键约定钉死：





给 AI 编程Agent一个确定入口



用 Markdown 承载可执行上下文



用分层机制适配大型仓库

在 AI Agent逐步变成“团队成员”的趋势下，这类基础设施会越来越像 .editorconfig 或 lint 配置一样：看似简单，却能持续减少沟通成本与返工。



参考链接





AGENTS.md 项目主页：https://agents.md/



Agentic AI Foundation：https://aaif.io/
