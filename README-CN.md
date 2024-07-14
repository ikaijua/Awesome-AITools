[English](README.md) | 中文

这个仓库整理AI相关的实用工具。

- [AI新闻动态](https://github.com/ikaijua/Awesome-AITools/discussions?discussions_q=is%3Aopen+label%3A%22AI+news%22)
## 全部分类
- [ChatGPT及类似闭源大语言模型](#chatgpt及类似闭源大语言模型)
- [开源大语言模型](#开源大语言模型)
- [GPT/LLMs 应用](#gpt-llms应用)
- [ChatGPT Prompts](#chatgpt-prompts)
- [国内可使用的ChatGPT镜像站点](#国内可使用的chatgpt镜像站点)
- [大语言模型排行榜](#大语言模型排行榜)
- [大语言模型训练-评估平台](#大语言模型训练-评估平台)
- [集成了多个大语言模型的应用](#集成了多个大语言模型的应用)
- [AI工具箱类软件](#ai工具箱类软件)
- [AI Agent](#ai-agent)
- [搜索引擎](#搜索引擎)
- [阅读](#阅读)
- [写作](#写作)
- [编程开发](#编程开发)
- [翻译工具](#翻译工具)
- [AI聊天-口语练习](#ai聊天-口语练习)
- [图像创作](#图像创作)
- [语音识别-生成字幕](#语音识别-生成字幕)
- [文字转语音](#文字转语音)
- [声音克隆](#声音克隆)
- [语音翻译](#语音翻译)
- [语音合成](#语音合成)
- [语音处理](#语音处理)
- [AI生成音乐-音效](#ai生成音乐-音效)
- [AI视频创作](#ai视频创作)
- [学术科研](#学术科研)
- [OCR图像识别文字](#ocr图像识别文字)
- [视频内容总结](#视频内容总结)
- [人形机器人](#人形机器人)

## 评测
- [大语言模型评测](#大语言模型评测)

## 精选文章
- [chatgpt相关文章](#chatgpt相关文章)

### ChatGPT及类似闭源大语言模型
| 名称 | 说明 | 链接 | 费用 | 
| ---- | ----------------------------- | --- | --- |
| ChatGPT | openAI的chatgpt </br>应用示例：</br> [B站视频：这9款工具帮你榨干ChatGPT，解锁隐藏玩法](https://www.bilibili.com/video/BV1qs4y1D7ED)</br> [B站视频：格斗之王！AI写出来的AI竟然这么强！](https://www.bilibili.com/video/BV1DT411H7ph) <br> [可汗学院创始人Khan最新TED演讲：GPT-4作为AI学习私教，可能带来教育史上最大变革](https://www.bilibili.com/video/BV1Xa4y137rR)|[URL](https://chat.openai.com)  | 免费/付费| 
| 微软Copilot | 微软的Copilot，包含了多种AI工具和插件 | [URL](https://copilot.microsoft.com/) | 免费 | 
| Claude|Anthropic研发的AI助手Claude|[URL](https://claude.ai/)| 免费|
| Gemini| Google 的对话式AI工具和最新的大语言模型，包括Gemini Nono，Gemini Pro和Gemini Ultra。Gemini Pro已开放api和sdk使用。api目前可免费使用，有每分钟60个请求的限制。[新闻介绍](https://github.com/ikaijua/Awesome-AITools/discussions/35#discussioncomment-7869696) |[Gemini AI聊天助手](https://bard.google.com/) <br>[Gemini api开发者网站](https://ai.google.dev/)|免费|
| Le Chat| Mistral AI 推出了为 Le Chat 的聊天助手 |[URL](https://chat.mistral.ai/chat)|免费|
| 豆包 | 字节跳动旗下的AI聊天软件 ; <br>体验测试视频：[B站视频：百模大战-抖音子公司推出AI聊天机器人豆包](https://www.bilibili.com/video/BV1b84y1o7E4/)|[URL](https://www.doubao.com/)|免费|
| 月之暗面的Kimi Chat|支持联网，支持上传文件（最多 50 个，每个 100 MB）接受 pdf、doc、xlsx、ppt、txt 等，文章总结能力比较强 <br>[张鹏对谈月之暗面杨植麟：大模型创业需要新的组织范式](https://www.xiaoyuzhoufm.com/episode/659d17352e26fb9934b8dceb)|[URL](https://kimi.moonshot.cn/)|免费|
| 文心一言 |百度的大语言模型|[URL](https://yiyan.baidu.com/)|免费|
| 通义千问 |阿里云的大语言模型 </br> 视频介绍： [B站视频：国产AI到底行不行？测试完通义千问，我只想说两个字【我们离ChatGPT还有多远】](https://www.bilibili.com/video/BV1KT411W7FN/)|[URL](https://tongyi.aliyun.com/)|免费|
| 智谱AI | 名为 ChatGLM 的人工智能助手，是基于清华大学 KEG 实验室和智谱 AI 公司于 2023 年共同训练的语言模型开发 | [URL](https://open.bigmodel.cn/)| 免费|
| 讯飞星火 | 讯飞的大语言模型| [URL](https://xinghuo.xfyun.cn/)| 免费|
| 百川大模型 | 百川智能的大语言模型 [开发者体验中心](https://platform.baichuan-ai.com/playground)| AI聊天助手：[百小应](https://ying.baichuan-ai.com/chat) | 免费 |
| 零一万物 |由李开复创办的AI公司，[零一万物 API 开放平台](https://platform.lingyiwanwu.com/)为新用户免费赠送60元api的使用额度，开源了模型Yi 6B和34B|[零一万物 API 开放平台](https://platform.lingyiwanwu.com/) <br> [Github](https://github.com/01-ai/Yi)  ![GitHub Repo stars](https://img.shields.io/github/stars/01-ai/Yi?style=social) |免费|
| 腾讯混元模型 |腾讯的大语言模型；[API文档](https://cloud.tencent.com/document/api/1729/105701)|[URL](https://hunyuan.tencent.com/bot)|免费|
| 中国国内发布的其他大模型|目前国内各大企业、科研机构和高校等单位已公开的 AI 大模型至少已经达到了 188 个。2023-12-17更新，[更多信息](https://github.com/ikaijua/Awesome-AITools/discussions/37#discussion-5968018)|||

### 开源大语言模型
| 名称 | 说明 | 链接 | 费用 | 
| ---- | ----------------------------- | --- | --- |
| Llama 3 | Llama3是Meta AI开发的开源的大型语言模型， 它是Llama 语言模型v3版本。<br>Llama3在线测试地址：[huggingface.co/Meta-Llama-3-70B-Instruct](https://huggingface.co/chat/models/meta-llama/Meta-Llama-3-70B-Instruct)|[GitHub](https://github.com/meta-llama/llama3) ![GitHub Repo stars](https://img.shields.io/github/stars/meta-llama/llama3?style=social)| 免费  | 
| Mixtral-8x7B |法国人工智能初创公司 Mistral AI开源的一种具有开放权重的稀疏专家混合模型 (SMoE)，在大多数基准测试中都优于 Llama 2 70B 和 GPT-3.5 <br>论文地址：https://arxiv.org/pdf/2401.04088.pdf <br>论文主页：https://mistral.ai/news/mixtral-of-experts/ |[Github](https://github.com/mistralai/mistral-src) ![GitHub Repo stars](https://img.shields.io/github/stars/mistralai/mistral-src?style=social)|免费|
|grok-1|马斯克的xAI公司开源的大语言模型|[Github](https://github.com/xai-org/grok-1) ![GitHub Repo stars](https://img.shields.io/github/stars/xai-org/grok-1?style=social)|免费|
| Qwen(通义千问)  |阿里云研发的通义千问大模型系列 <br>在线Demo地址：<br> [Qwen-7B-Chat-Demo](https://modelscope.cn/studios/qwen/Qwen-7B-Chat-Demo/summary) <br> [Qwen-72B-Chat-Demo](https://modelscope.cn/studios/qwen/Qwen-72B-Chat-Demo/summary) <br>[Qwen1.5 72B 在线体验](https://huggingface.co/spaces/Qwen/Qwen1.5-72B-Chat)| [Qwen-7B](https://github.com/QwenLM/Qwen-7B) ![GitHub Repo stars](https://img.shields.io/github/stars/QwenLM/Qwen-7B?style=social)<br>[Qwen1.5](https://github.com/QwenLM/Qwen1.5)![GitHub Repo stars](https://img.shields.io/github/stars/QwenLM/Qwen1.5?style=social)| 免费  | 
| ChatGLM2-6B | 中英双语对话模型 ChatGLM-6B 的第二代版本 | [GitHub](https://github.com/THUDM/ChatGLM2-6B) ![GitHub Repo stars](https://img.shields.io/github/stars/THUDM/ChatGLM2-6B?style=social)| 免费|
| Phi-3| Phi-3是微软开发的开放式人工智能模型系列。Phi-3 模型是目前能力最强、最具成本效益的小型语言模型（SLM），在各种语言、推理、编码和数学基准测试中，其性能均优于相同大小和更大的模型。|[Github](https://github.com/microsoft/Phi-3CookBook) ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/Phi-3CookBook?style=social)|免费|

### GPT-LLMs应用
| 名称 | 说明 | 链接 | 费用 | 
| ---- | ----------------------------- | --- | --- |
| Poe | 美版知乎 Quora 构建的AI 产品，有web和客户端。目前的情况是ChatGPT、Sage、Dragonfly、Claude 机器人可以免费、无限制、实时使用。只需要一个邮箱即可注册。可以随时切换AI而对话不中断，并且对话记录是在线保存并且同步到客户端的。chatgpt-4可以每天免费使用一次 </br> 视频介绍：[B站视频：神器！与chatGPT类似的新人工智能问答AI：Poe, 美国知乎Quaro最新产品，专业回答](https://www.bilibili.com/video/BV13Y411B7Az)| [URL](https://poe.com/) |免费，有付费升级版|
| monica | AI助手，提供搜索、阅读、写作、翻译、绘画等多种任务的帮助。有独立应用和浏览器插件| [URL](https://monica.im) <br> [chrome插件](https://chromewebstore.google.com/detail/monica-your-ai-copilot-po/ofpnmcalabcbjgholdjcjblkibolbppb)|免费/付费|
| ollama | 在本地环境中轻松运行和管理大型语言模型，如Llama 、Mistral、Gemma2等|[Github](https://github.com/ollama/ollama) ![GitHub Repo stars](https://img.shields.io/github/stars/ollama/ollama?style=social)	|免费|
| openai/openai-python | OpenAI API 的官方 Python 库，它是使用[Stainless](https://stainlessapi.com/)根据[OpenAPI 规范]((https://github.com/openai/openai-openapi))生成的 | [Github](https://github.com/openai/openai-python)![GitHub Repo stars](https://img.shields.io/github/stars/abi/screenshot-to-code?style=social)| 免费，需要使用OpenAPI的[apikey](https://platform.openai.com/account/api-keys) |
|sashabaranov/go-openai|OpenAI API的Go语言非官方的SDK，支持ChatGPT、GPT-3、 GPT-4、DALL·E 2|[Github](https://github.com/sashabaranov/go-openai)![GitHub Repo stars](https://img.shields.io/github/stars/sashabaranov/go-openai?style=social)|免费|
|langchain|是一个强大的框架，旨在帮助开发人员使用语言模型构建端到端的应用程序。它提供了一套工具、组件和接口，可简化创建由大型语言模型 (LLM) 和聊天模型提供支持的应用程序的过程。LangChain 可以轻松管理与语言模型的交互，将多个组件链接在一起，并集成额外的资源，例如 API 和数据库。|[Github](https://github.com/langchain-ai/langchain) ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/langchain?style=social)|免费|
|ChatGPT-Next-Web|一键免费部署你的跨平台私人 ChatGPT 应用, 支持 GPT3, GPT4 & Gemini Pro 模型|[Github](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web) ![GitHub Repo stars](https://img.shields.io/github/stars/ChatGPTNextWeb/ChatGPT-Next-Web?style=social)|免费|
|anything-llm|开源的文档聊天机器人解决方案|[Github](https://github.com/Mintplex-Labs/anything-llm) ![GitHub Repo stars](https://img.shields.io/github/stars/Mintplex-Labs/anything-llm?style=social)|免费|
| screenshot-to-code | 插入截图并将其转换为简洁的 HTML/Tailwind/JS 代码，使用了GPT-4 Vision来生成代码，使用DALL-E 3生成图片 | [GitHub](https://github.com/abi/screenshot-to-code) ![GitHub Repo stars](https://img.shields.io/github/stars/abi/screenshot-to-code?style=social)| 免费，需要有GPT-4 Vision的授权|
| Chatbox | 使用ChatGPT API（OpenAI API）的桌面应用程序, 将所有的聊天信息和提示信息存储在本地，从而减少了数据丢失的风险。比网页版使用更稳定些| [GitHub](https://github.com/Bin-Huang/chatbox) ![GitHub Repo stars](https://img.shields.io/github/stars/Bin-Huang/chatbox?style=social)| 免费，需要使用OpenAPI的[apikey](https://platform.openai.com/account/api-keys)|
| ChatGPT for Google |开源项目，浏览器插件，在搜索页面增加chatgpt的内容和对话框|[GitHub](https://github.com/wong2/chatgpt-google-extension) ![GitHub Repo stars](https://img.shields.io/github/stars/wong2/chatgpt-google-extension?style=social)|免费，需要chatgpt账号|
| gpt-crawler | 可以爬取指定网站中的内容，并生成json文件，可以直接上传到GPTs的知识库使用 | [Github](https://github.com/BuilderIO/gpt-crawler)![GitHub Repo stars](https://img.shields.io/github/stars/BuilderIO/gpt-crawler?style=social)| 免费|
| ChatGPT-Shortcut | 开源，让生产力加倍的 ChatGPT 快捷指令，按照领域和功能分区，可对提示词进行标签筛选、关键词搜索和一键复制。| [GitHub](https://github.com/rockbenben/ChatGPT-Shortcut) ![GitHub Repo stars](https://img.shields.io/github/stars/rockbenben/ChatGPT-Shortcut?style=social)|免费| 
|ChatGPT Sidebar|ChatGPT 边栏是您在浏览任何网站时可以使用的人工智能助手。</br> 视频介绍：[B站视频：CharGPT初体验，浏览器安装人工智能侧边栏AI Sidebar扩展程序](https://www.bilibili.com/video/BV1Y24y1L7JA)|[URL](https://chrome.google.com/webstore/detail/chatgpt-sidebar-support-g/difoiogjjojoaoomphldepapgpbgkhkb)|免费|
| WebChatGPT |开源程序，给chatgpt扩展联网的能力 </br> 视频介绍：[B站视频：可以让ChatGPT直接联网的扩展程序](https://www.bilibili.com/video/BV1bY4y1C7N3) | [GitHub](https://github.com/qunash/chatgpt-advanced) ![GitHub Repo stars](https://img.shields.io/github/stars/qunash/chatgpt-advanced?style=social)| 免费|
| AIPRM for ChatGPT |浏览器插件，提供一系列精选ChatGPT 指令模板，甚至还能够自己创建，还可以调整AI 语气和写作风格 </br>B站视频：[集大成者！ChatGPT百宝箱，内置多种功能，所见即所得！](https://www.bilibili.com/video/BV1LT411S7GK)| [URL](https://chrome.google.com/webstore/detail/aiprm-for-chatgpt/ojnbohmppadfgpejeebfnmnknjdlckgj) | 免费|
| GPTCache |⚡ GPTCache 是一个用于创建语义缓存以存储来自 LLM 查询的响应的库，类似于aigc场景中的redis。 它可用于降低依赖 LLM 服务（如ChatGPT）的成本，同时也可以有效减少服务响应时间，因为大模型推理一般都比较耗时。| [GitHub](https://github.com/zilliztech/GPTCache) ![GitHub Repo stars](https://img.shields.io/github/stars/zilliztech/GPTCache?style=social)| 免费|
| MindMac | 功能丰富、隐私第一的 macOS 原生 ChatGPT 应用程序，可在一个地方使用 OpenAI, Azure OpenAI, Anthropic Claude, OpenRouter，旨在实现最大生产力。 目前有 15 种语言版本。| [URL](https://mindmac.app/) | 免费，有付费升级版 |

### ChatGPT Prompts
| 名称 | 说明 | 链接 |费用|
| ---- | ----------------------------- | --- | --- |
|f/awesome-chatgpt-prompts|This repo includes ChatGPT prompt curation to use ChatGPT better.|[Github](https://github.com/f/awesome-chatgpt-prompts) ![GitHub Repo stars](https://img.shields.io/github/stars/f/awesome-chatgpt-prompts?style=social) |Free|

### 国内可使用的ChatGPT镜像站点
| 名称 | 说明 | 链接 |
| ---- | ----------------------------- | --- | 
| carrot | Free ChatGPT Site List 这儿为你准备了众多免费好用的ChatGPT镜像站点，当前100+站点国内可使用ChatGPT镜像站点 | [GitHub](https://github.com/xx025/carrot) </br>![GitHub Repo stars](https://img.shields.io/github/stars/xx025/carrot?style=social)|
| awesome-free-chatgpt | 免费的 ChatGPT 镜像网站列表，持续更新。List of free ChatGPT mirror sites, continuously updated. | [GitHub](https://github.com/LiLittleCat/awesome-free-chatgpt)  </br> ![GitHub Repo stars](https://img.shields.io/github/stars/LiLittleCat/awesome-free-chatgpt?style=social)|

### 大语言模型排行榜
| Name | Description | Links | Fees | 
| ---- | ----------------------------- | --- | --- |
|LMSYS Chatbot Arena Leaderboard|LMSYS Chatbot Arena 是一个用于大语言模型评估的众包开放平台。收集了超过 1,000,000 次人类成对比较，用 Bradley-Terry 模型对 LLM 进行排名，并以 Elo 标度显示模型评级。<br>B站视频：[量子位/1v1单挑90万轮之后，最强大模型是……](https://www.bilibili.com/video/BV1Qs421w7df/) |[URL](https://chat.lmsys.org/) |免费|
|Artificial Analysis|Artificial Analysis 是一个提供 AI 模型和服务商比较及基准测试的资源平台，帮助用户在选择 AI 模型和服务提供商时做出明智决策。平台提供多种流行 AI 模型的比较数据，包括 OpenAI 的 GPT-4、Meta 的 Llama 3 和 Anthropic 的 Claude 系列，涵盖了响应速度、延迟和成本等性能指标。|[URL](https://artificialanalysis.ai/)|免费|

### 大语言模型训练-评估平台
| Name | Description | Links | Fees |
| ---- | ----------------------------- | --- | --- |
| FastChat | 用于训练、服务和评估大型语言模型的开放平台。Vicuna 和 Chatbot Arena 的发布仓库。| [Github](https://github.com/lm-sys/FastChat) ![GitHub Repo stars](https://img.shields.io/github/stars/lm-sys/FastChat?style=social)| Free |

### 集成了多个大语言模型的应用
| 名称 | 说明 | 链接 | 费用 |
| ---- | ----------------------------- | --- | ---- |
| chathub | 浏览器插件，在一个应用中使用不同的聊天机器人，目前支持 ChatGPT、新的 Bing Chat、Google Bard 和 Claude (via Poe)，未来将集成更多机器人， 同时与多个聊天机器人聊天，方便比较它们的答案 | [GitHub](https://github.com/chathub-dev/chathub) </br>![GitHub Repo stars](https://img.shields.io/github/stars/chathub-dev/chathub?style=social)|免费，付费支持更多功能|
| ChatALL | 同时与多个大语言模型聊天的客户端（支持Windows、macOS、Linux系统），支持ChatGPT、Bing Chat、Claude、Bard、MOSS、Alpaca、HuggingChat等。需要拥有可以访问这些 AI 的帐号，或 API token| [GitHub](https://github.com/sunner/ChatALL)  </br> ![GitHub Repo stars](https://img.shields.io/github/stars/sunner/ChatALL?style=social)|免费|


### AI工具箱类软件
| 名称 | 说明 | 链接 | 费用 | 
| ---- | ----------------------------- | --- | --- |
|Paper2GUI|一款面向普通人的 AI 桌面 APP 工具箱，免安装即开即用，已支持 40+AI 模型，内容涵盖 AI 绘画、语音合成、视频补帧、视频超分、目标检测、图片风格化、OCR 识别等领域。支持 Windows、Mac、Linux 系统。</br>[B站视频介绍：补帧超分抠图配音，这个开源AI工具箱对小白太友好了！](https://www.bilibili.com/video/BV1jY411u7yU/)|[GitHub](https://github.com/Baiyuetribe/paper2gui) ![GitHub Repo stars](https://img.shields.io/github/stars/Baiyuetribe/paper2gui?style=social)|免费|

### AI Agent
| 名称 | 说明 | 链接 | 费用 | 
| ---- | ----------------------------- | --- | --- |
|Auto-GPT|开源项目，使用gpt自主地实现你设定的任何目标。演示示例：[爆火的自主人工智能AutoGPT，程序员表示开始真正有点担忧会失业了！](https://www.bilibili.com/video/BV1Ph4y1W7Yj)|[GitHub](https://github.com/Torantulino/Auto-GPT) ![GitHub Repo stars](https://img.shields.io/github/stars/Torantulino/Auto-GPT?style=social)|免费，需要OpenAI API key|
|OthersideAI/self-operating-computer|一个使用多模态模型（默认模型为GPT-4v）能够操作计算机的框架|[Github](https://github.com/OthersideAI/self-operating-computer) ![GitHub Repo stars](https://img.shields.io/github/stars/OthersideAI/self-operating-computer?style=social)|免费，需要GPT-4v|
|AppAgent|可以操作手机应用程序的AI Agent|[Github](https://github.com/mnotgod96/AppAgent) ![GitHub Repo stars](https://img.shields.io/github/stars/mnotgod96/AppAgent?style=social)|免费|

### 搜索引擎
| 名称 | 说明 | 链接 | 费用 | 
| --- | --- | --- | --- |
| You.com | 结合对话模式的搜索引擎 | [URL](https://you.com) | 免费 |
| Perplexity.ai | Perplexity.ai 是一个基于 GPT-3 的 AI 工具，类似 New Bing 的搜寻引擎、会附上参考结果 | [URL](https://www.perplexity.ai) | 免费|

### 阅读
| 名称 | 说明 | 链接 | 费用 | 
| --- | --- | --- | --- |
| 微信读书 | “AI问书”功能，在阅读时遇到不理解的内容，可以通过AI问书功能获得即时解释。AI问书的回答通常包含注释和相关书籍推荐，并且可以通过点击回答中的链接跳转到相关书籍的特定选段，增加回答的可信度[更多介绍](https://github.com/ikaijua/Awesome-AITools/discussions/77#discussioncomment-9559619) | [URL](https://weread.qq.com/) | 免费/付费 | 

### 写作
| 名称 | 说明 | 链接 | 费用 | 
| ---- | ----------------------------- | --- | --- |
| Notion AI | AI辅助的笔记软件，主要包括AI创作文章、翻译、修正语法、摘要和总结等 </br> 视频示例：[B站视频：Notion AI完整介绍 \| 十个节省时间的神功能(ChatGPT般强大)](https://www.bilibili.com/video/BV1Lg411b7Cx) | [URL](https://www.notion.so)| 有一定免费的AI试用次数，AI功能10$/每月 |
| verse | 印象笔记推出的AI写作工具 |[URL](https://verse.app.yinxiang.com/product)|免费|
| 写作猫 | 集AI写作、多人协作、文本校对、改写润色、自动配图等功能为一体AI Native内容创作平台| [URL](https://xiezuocat.com/)| 免费|
| Deep L Write | 英文、德文写作工具，可以及時修正写作錯誤、改写句子。 | [URL](https://www.deepl.com/write) |  免費版本使用有文字字数限制/有付费升级版 |
| grammarly | 纠正语法、拼写、标点符号等错误的写作助手| [URL](https://app.grammarly.com/) | 免费/有付费升级版|
| 火山写作 | 写作润色、翻译 | [URL](https://www.writingo.net/document) |免费|

### 编程开发
| 名称 | 说明 | 链接 | 费用 | 
| ---- | ----------------------------- | --- | --- | 
| GitHub Copilot | GitHub 和 OpenAI 合作开发的一个代码编写助手 </br>[Github Copilot技巧和窍门](https://bilibili.com/video/BV1ic411T7Jd) </br>[Github Copilot X的Chat功能介绍](https://www.bilibili.com/video/BV1Ho4y137Tu/)，[Copilot X申请页面](https://github.com/features/preview/copilot-x)| [URL](https://github.com/features/copilot)  | 付费 |
| 通义灵码|阿里云开发的代码编写助手，可根据当前代码文件及跨文件的上下文，为你生成行级/函数级代码、单元测试、代码注释等，支持 Java、Python、Go、JavaScript、TypeScript、C/C++、C# 等主流语言，同时兼容 Visual Studio Code、JetBrains IDEs 等主流编程工具|[URL](https://tongyi.aliyun.com/lingma/)|免费|
| CodeGeeX | 智谱AI旗下的代码生成大模型，支持200多种主流编程语言的生成及翻译。开源模型：<br>[CodeGeeX2](https://github.com/THUDM/CodeGeeX2/) ![GitHub Repo stars](https://img.shields.io/github/stars/THUDM/CodeGeeX2?style=social) <br>[CodeGeex4](https://github.com/THUDM/CodeGeeX4) ![GitHub Repo stars](https://img.shields.io/github/stars/THUDM/CodeGeeX4?style=social)</br> [【项目原作解读】清华大学郑勤锴：CodeGeeX大规模多语言代码生成模型](https://www.bilibili.com/video/BV1wT41127Tq/) | [URL](https://codegeex.cn/) |免费|
| Cursor | 使用 GPT进行协作的代码编辑器 | [URL](https://www.cursor.so) | 免费 |
| ai-code-translator   | 利用chatgpt将代码从一种语言翻译成另一种语言。| [GitHub](https://github.com/mckaywrigley/ai-code-translator) ![GitHub Repo stars](https://img.shields.io/github/stars/mckaywrigley/ai-code-translator?style=social) | 免费，需要OpenAI API key|
| Amazon CodeWhisperer | 亚马逊开放的AI编程辅助工具，根据你的注释和现有代码，实时生成从片段到完整功能的代码建议。在各种IDE的插件中可以安装,支持15种语言, 包括 Python, Java, and JavaScript等。只需要按照流程注册一个aws builder账号即可。| [URL](https://aws.amazon.com/cn/codewhisperer)| 免费|
| Fitten Code | Fitten Code是由非十大模型驱动的AI编程助手，可以自动生成代码，提升开发效率，调试Bug。还可以对话聊天，解决您编程碰到的问题。免费且支持80多种语言：Python、C++、Javascript、Typescript、Java等。并提供丰富的IDE支持，包括Visual Studio Code、JetBrains系列IDE等。<br>“技术胖”B站视频：[清华初创对决微软Github，哪家AI编程助手更强](https://www.bilibili.com/video/BV1MH4y1s7sU/)| [URL](https://code.fittentech.com/) | 免费 |
|gpt-engineer|一个根据指示生成代码的AI工具，能直接构建整个代码库。[B站上的介绍演示视频：gpt-engineer：100%替代程序员的AI程序员来了...](https://www.bilibili.com/video/BV1Da4y1w7Tk/)|[GitHub](https://github.com/AntonOsika/gpt-engineer) ![GitHub Repo stars](https://img.shields.io/github/stars/AntonOsika/gpt-engineer?style=social)|免费|
|flappy|一个产品级面向所有程序员的LLM SDK|[GitHub](https://github.com/pleisto/flappy) ![GitHub Repo stars](https://img.shields.io/github/stars/pleisto/flappy.svg?style=social) |免费|
|腾讯云AI代码助手|腾讯云 AI 代码助手主要提供两类功能：AI 助手对话功能和代码补全功能。|[URL](https://console.cloud.tencent.com/acc)|免费|
|Mistral/Codestral|Mistral.ai的代码生成大语言模型，官方介绍：[Empowering developers and democratising coding with Mistral AI.](https://mistral.ai/news/codestral/), 模型下载:https://huggingface.co/mistralai/Codestral-22B-v0.1|[URL](https://chat.mistral.ai/chat) 模型选择Codestral|免费|

### 翻译工具
| 名称 | 说明 | 链接 | 费用 | 
| ---- | ----------------------------- | --- | --- |
| immersive-translate | 开源的，沉浸式双语网页翻译扩展 | [GitHub](https://github.com/immersive-translate/immersive-translate/) ![GitHub Repo stars](https://img.shields.io/github/stars/immersive-translate/immersive-translate?style=social) | 免费 |
| Deep L | 准确即时的翻译工具，目前支持 31 种语言 | [URL](https://www.deepl.com/translator) | 免费/付费
| openai-translator | 基于 ChatGPT API 的划词翻译浏览器插件和跨平台桌面端应用 | [GitHub](https://github.com/yetone/openai-translator) ![GitHub Repo stars](https://img.shields.io/github/stars/yetone/openai-translator?style=social)| 免费，需要OpenAI API key |

### AI聊天-口语练习

| 名称 | 说明 | 链接 | 费用 | 
| ---- | ----------------------------- | --- | --- |
| pi.ai | 一个公认很会聊天的AI，不用担心把天聊死了，并且支持文字和语音。语音输入需要借助苹果系统自带的输入。很适合练习英语对话和听力| [URL](https://pi.ai) | 免费 |
|Voice Control for ChatGPT | chrome扩展程序，通过它可以与 ChatGPT 进行语音对话。可以帮助英语口语或其他语言口语练习。</br>视频示例：[B站视频:免费口语老师：如何用ChatGPT练习英语口语](https://www.bilibili.com/video/BV1iy4y1Q7Fh) | [URL](https://chrome.google.com/webstore/detail/voice-control-for-chatgpt/eollffkcakegifhacjnlnegohfdlidhn) | 免费，需要chatgpt账号  | 
|SpeechGPT|开源项目，SpeechGPT 是一个让你与 ChatGPT 聊天的网站。|[GitHub](https://github.com/hahahumble/speechgpt) ![GitHub Repo stars](https://img.shields.io/github/stars/hahahumble/speechgpt?style=social)|免费，需要OpenAI API key|


### 图像创作
| 名称 | 说明 | 链接 | 费用 | 
| ---- | ----------------------------- | --- | --- |
| Midjourney | 输入文字或图片进行图片创作。应用示例：<br> [尝试用chatGPT+midjourney进行科研绘图，被效果震惊到了。。。](https://www.bilibili.com/video/BV1XM411T7uP) | [URL](https://www.midjourney.com) | 付费 |
| Stable diffusion webui | 开源项目，输入文字或图片进行图片创作， Stable diffusion webui是Stable diffusion的GUI是将stable diffusion实现可视化的图像用户操作界面，它本身还集成了很多其它有用的扩展脚本。<br>新手入门教程：https://www.bilibili.com/video/BV1Qo4y167AK/ </br> AI风格化视频或AI真人视频的效果：</br>1. [【AI动画】欣小萌天台蹦迪 动画版](https://www.bilibili.com/video/BV1RL411U7wR)，</br>2. [死磕真人AI动作，人物和背景的终于不闪了，你们觉得哪个更好点？](https://www.bilibili.com/video/BV1Fs4y1V7f7)</br>3. [5分钟，教会你如何生成AI动画](https://www.bilibili.com/video/BV13s4y1D7Ni)| [GitHub](https://github.com/AUTOMATIC1111/stable-diffusion-webui) ![GitHub Repo stars](https://img.shields.io/github/stars/AUTOMATIC1111/stable-diffusion-webui?style=social)| 免费|
| 即梦AI|字节跳动旗下的文生图、AI视频生成和AI图片编辑应用|[URL](https://jimeng.jianying.com/ai-tool/home)|免费/付费|
| Photoshop 生成式AI功能| 在Adobe Photoshop中使用生成式AI填充功能。功能介绍：</br> 1. [B站视频：Photoshop 革命性新功能-生成式填充功能介绍](https://www.bilibili.com/video/BV1su411Y79Z/) <br> 2. [巫师后期B站视频：引爆点——Photoshop核弹级更新（创成式AI填充）彻底改变图片行业！](https://www.bilibili.com/video/BV1qo4y1E7tK)| [URL](https://www.adobe.com/products/photoshop/generative-fill.html) |Photoshop 订阅会员可下载Beta版本试用|
| firefly |Adobe 的AI图片处理网站|[URL](https://firefly.adobe.com/)|免费/付费|
| clipdrop | stability.ai 公司旗下的图像处理网站，包含文生图、AI扩图、图生图、去除背景等功能 | [URL](https://clipdrop.co/)| 免费/ 付费|
| civitai | Civitai(C站)是一个用于分享AI图像创作模型资源的网站平台，拥有大量模型，已成为SD开源社区主要的模型交流场所 |[URL](https://civitai.com/)|免费|
| 文心一格 | 百度旗下的文生图和AI图片编辑应用| [URL](https://yige.baidu.com/)| 免费/付费 |
| 通义万相 | 阿里旗下的文生图和AI图片创作应用| [URL](https://wanxiang.aliyun.com/) | 免费 |
| 美图的奇想智能MiracleVision|美图的文生图应用|[URL](https://www.miraclevision.com/text-to-image/)|免费|
| ideogram.ai | AI 文字生成图片的网站。前谷歌AI绘画4位大牛创立的公司推出的产品 | [URL](https://ideogram.ai/) | 免费 |
| Skybox AI | 输入文字生成360度全景图片 | [URL](https://skybox.blockadelabs.com/)| 免费/ 付费|
| Microsoft Bing Image Creator | Image Creator 是使用 DALL-E 技术创作图片的工具。试用了下**生成人像图片不堪入目** | [URL](https://www.bing.com/images/create) | 免费|
| remove.bg |一键删除图片背景|[URL](https://www.remove.bg/)|免费/付费|
| 简单AI | 搜狐旗下的文生图和图片分享网站 | [URL](https://ai.sohu.com/) | 免费/付费 |
|ControlNet|能够在一个text2image上训练的扩散模型进行高效finetune，并且结合特定的condition输入，得到可控的效果|[Github](https://github.com/lllyasviel/ControlNet) ![GitHub Repo stars](https://img.shields.io/github/stars/lllyasviel/ControlNet?style=social)|免费|
|StreamDiffusion| 实时AI互动图片生成的管道级解决方案|[Github](https://github.com/cumulo-autumn/StreamDiffusion) ![GitHub Repo stars](https://img.shields.io/github/stars/cumulo-autumn/StreamDiffusion?style=social)|免费|
| visual-chatgpt | 通过 ChatGPT 创作图片 | [GitHub](https://github.com/microsoft/visual-chatgpt) ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/visual-chatgpt?style=social) | 免费 
|DragGAN|一种新的交互式图像编辑方法，允许用户通过简单地在图像上点击并拖动点来进行编辑|[GitHub](https://github.com/XingangPan/DragGAN) </br> ![GitHub Repo stars](https://img.shields.io/github/stars/XingangPan/DragGAN?style=social)|免费|

### 语音识别-生成字幕
| 名称 | 说明 | 链接 | 费用 | 
| ---- | ----------------------------- | --- | --- | 
| whisper | 开源，OpenAPI 开源的通过大规模的弱监督进行鲁棒性的语音识别的模型 | [GitHub](https://github.com/openai/whisper) ![GitHub Repo stars](https://img.shields.io/github/stars/openai/whisper?style=social) | 免费 |
| buzz | 开源，基于OpenAI的Whisper识别语音并生成字幕的开源桌面软件，使用CPU进行处理 | [GitHub](https://github.com/chidiwilliams/buzz) ![GitHub Repo stars](https://img.shields.io/github/stars/chidiwilliams/buzz?style=social)| 免费 |
| WhisperDesktop| 开源，基于OpenAI的Whisper，Windows系统的桌面应用，使用GPU进行处理，GPU性能好的话会比CPU上更快。使用介绍：https://www.appinn.com/const-me-whisper/|[GitHub](https://github.com/Const-me/Whisper) ![GitHub Repo stars](https://img.shields.io/github/stars/Const-me/Whisper?style=social)|免费|
| whisperX | 开源，一位来自牛津大学的博士生Max Bain开源的模型，WhisperX可以按照单词对齐时间戳，**基本上生成的字幕都是完整的句子**。生成结果除了srt还有json文件，里面有每一行里面单词的时间戳，可以根据需要二次整理字幕。还能识别发言人，准确率还可以。使用示例：</br> 1. **在google colab上使用whisperX生成youtube视频字幕的代码**：[whisperx_youtube_subtitle](https://github.com/JimLiu/whisper-subtitles/blob/main/whisperx_youtube_subtitle.ipynb)，可以免费使用colab的GPU，使用GPU T4，2小时40分钟的视频字幕生成6分钟左右，挺快的。| [whisperX](https://github.com/m-bain/whisperX) ![GitHub Repo stars](https://img.shields.io/github/stars/m-bain/whisperX?style=social) |免费|
| 飞书秒记 | 上传视频或者音频可转录为文字，并可一键导出到飞书文档。处理速度很快，一个将近 2 个多小时的视频，约 6 分钟完成。 | [URL](https://www.feishu.cn/product/minutes)| 免费，有企业付费版|
| 通义听悟 | 阿里旗下的语音转录应用 | [URL](https://tingwu.aliyun.com/) | 免费/付费 |
| whisper-web | 在浏览器中运行ML驱动的语音识别! 使用[Transformers.js](https://github.com/xenova/transformers.js)构建。[Demo链接](https://huggingface.co/spaces/Xenova/whisper-web) | [GitHub](https://github.com/xenova/whisper-web) ![GitHub Repo stars](https://img.shields.io/github/stars/xenova/whisper-web?style=social)|免费|

### 文字转语音
| 名称 | 说明 | 链接 | 费用 | 
| ---- | ----------------------------- | --- | --- | 
| 微软Azure 文本转语音| 目前最好用最真实的语音工具，包括自媒体配音最常见的云希和晓晓的声音；<br>效果演示：[痕继痕迹:啊？这是AI合成的？- 盘点那些超逼真的AI语音！](https://www.bilibili.com/video/BV1DC411G7Av/)</br>教程：[免费使用微软的Azure；Azure使用详细教程](https://www.youtube.com/watch?v=YzNfMY_oqhA);| [URL](https://speech.microsoft.com/portal/voicegallery) |付费/每个月有50万字符的免费额度|
| 剪映 |文本朗读有很多的音色选择|[URL](https://www.capcut.cn/)|免费/vip|
| TTS-Online | 提供超过160种声音选项 美真人配音选择，包含主流的小帅 小美 微软的一些语音，如果你是二次元游戏迷之类网站还提供超过1000+的动漫游戏角色的声音。网站可以提供api。分享者：[issue](https://github.com/ikaijua/Awesome-AITools/issues/31) | [URL](https://www.ttson.cn/)|免费 |
| 火山引擎TTS| 火山引擎的语音合成| [URL](https://www.volcengine.com/product/tts)|付费|
| 配音神器 | 有网页端、windows客户端工具，使用比较方便 |[URL](https://peiyinshenqi.club/)|付费/非 VIP 每天可试用 5 次|
| coqui-ai/tts | 用于文本到语音的深度学习工具包 <br> 在线体验Demo网页：https://huggingface.co/spaces/coqui/xtts| [Github](https://github.com/coqui-ai/tts) ![GitHub Repo stars](https://img.shields.io/github/stars/coqui-ai/tts?style=social) | 免费|
| elevenlabs | 文字转语音的服务，提供多种语言 |[URL](https://elevenlabs.io/)|免费/付费|
| netease-youdao/EmotiVoice | EmotiVoice是一个强大的开源TTS引擎，支持中英文双语，包含2000多种不同的音色，以及特色的情感合成功能，支持合成包含快乐、兴奋、悲伤、愤怒等广泛情感的语音。|[Github](https://github.com/netease-youdao/EmotiVoice) ![GitHub Repo stars](https://img.shields.io/github/stars/netease-youdao/EmotiVoice?style=social)| Free|
| tetos |适用于多个文本转语音 （TTS） 提供程序的统一接口，支持Edge TTS、OpenAI TTS、Azure TTS、Google TTS、火山引擎TTS、百度TTS|[Github](https://github.com/frostming/tetos) ![GitHub Repo stars](https://img.shields.io/github/stars/frostming/tetos?style=social)|免费|
| ChatTTS |ChatTTS是专门为对话场景设计的文本转语音模型，例如LLM助手对话任务。它支持英文和中文两种语言。最大的模型使用了10万小时以上的中英文数据进行训练。官网：https://chattts.com/|[Github](https://github.com/2noise/ChatTTS)![GitHub Repo stars](https://img.shields.io/github/stars/2noise/ChatTTS?style=social)|免费|

### 声音克隆
| 名称 | 说明 | 链接 | 费用 | 
| ---- | ----------------------------- | --- | --- | 
| 剪映 |目前只有APP端有声音克隆的功能，朗读一小段文字就能完成音色的克隆，音色效果很牛。当你添加文本时，在“文本朗读”那个功能中，点击“我的”tab，就能看到这个功能了|[URL](https://www.capcut.cn/)|限免|
| 豆包 |字节跳动的AI聊天应用，豆包app中声音设置可以选择“创建我的声音”，回答问题的时候就可以用克隆的声音来回答了|[URL](https://www.doubao.com/)|免费|

### 语音翻译
| 名称 | 说明 | 链接 | 费用 | 
| ---- | ----------------------------- | --- | --- | 
| Seamless |可以实时翻译100多种语言，延迟不到2秒钟，说话者仍在讲话时就开始翻译。Seamless翻译不仅仅是文字上的转换，还能保持说话者的情感和语气、语调等，使得翻译后的语音更加自然和真实。Seamless模型统一了SeamlessExpressive、SeamlessStreaming和SeamlessM4T v2的功能。旨在实现多语言、表达性和流畅的语音翻译。在线体验[Demo地址](https://seamless.metademolab.com/expressive?utm_source=metaai&utm_medium=web&utm_campaign=fair10&utm_content=blog)|[Github](https://github.com/facebookresearch/seamless_communication) ![GitHub Repo stars](https://img.shields.io/github/stars/facebookresearch/seamless_communication?style=social)|Free|

### 语音合成
| 名称 | 说明 | 链接 | 费用 | 
| ---- | ----------------------------- | --- | --- | 
|so-vits-svc| So-vits-svc（也称Sovits）是基于VITS、soft-vc、VISinger2等一系列项目开发的一款开源免费 AI 语音转换软件，用户只需准备几十分钟到几个小时不等的语音或歌声数据，就能制作属于自己的 AI 声库，将一段语音或歌声转换为你想要的音色。[更多介绍](https://zh.moegirl.org.cn/zh-hans/So-vits-svc) </br> [B站视频：手把手教学！如何自己训练一个AI歌手 - sovits本地&云端训练教程](https://www.bilibili.com/video/BV1ea4y1G7gx)|[GitHub](https://github.com/svc-develop-team/so-vits-svc) ![GitHub Repo stars](https://img.shields.io/github/stars/svc-develop-team/so-vits-svc?style=social)|免费|
|open-mmlab/Amphion|开源音频、音乐和语音生成工具包， 在线使用：https://huggingface.co/amphion <br> 文章介绍：机器之心：[霉霉演唱《稻香》，国内团队的Amphion音频生成火了](https://mp.weixin.qq.com/s/2oR7tu-ltnXnZqNCi-unlA)| [Github](https://github.com/open-mmlab/Amphion) ![GitHub Repo stars](https://img.shields.io/github/stars/open-mmlab/Amphion?style=social)|免费|

### 语音处理
| 名称 | 说明 | 链接 | 费用 | 
| ---- | ----------------------------- | --- | --- | 
|vocalremover|分离人声和伴奏|[URL](https://vocalremover.org/)|有免费的试用额度/付费|
|lala.ai|从任何音频和视频中提取人声、伴奏和各种乐器|[URL](https://www.lalal.ai/)|有免费的试用额度/付费|

### AI生成音乐-音效
| 名称 | 说明 | 链接 | 费用 | 
| ---- | ----------------------------- | --- | --- |
|suno.ai|使用AI通过文本来创作音乐 [suno专题页面](https://github.com/ikaijua/Awesome-AITools/discussions/63)<br>应用示例：<br> 韩雪：[【AI音乐家】我在古镇用AI写歌！](https://www.bilibili.com/video/BV13a4y1m7A5/) <br> |[URL](https://www.suno.ai/)|免费/付费|
|udio|使用AI通过文本来创作音乐|[URL](https://www.udio.com/)|免费/付费|
|elevenlabs/sound-effects|elevenlabs 提供的通过文本生成音效的工具|[URL](https://elevenlabs.io/app/sound-effects)|免费|
|suno-ai/bark|文本转音频模型|[Github](https://github.com/suno-ai/bark) ![GitHub Repo stars](https://img.shields.io/github/stars/suno-ai/bark?style=social)|免费|
|audiocraft|Meta开源的一个用于音频/音乐生成的开源库，其中主要包括两个模型，MusicGen：文本到音乐模型，AudioGen：文本生成声音模型。[MusicGen在线Demo](https://huggingface.co/spaces/facebook/MusicGen)|[GitHub](https://github.com/facebookresearch/audiocraft) <br>![GitHub Repo stars](https://img.shields.io/github/stars/facebookresearch/audiocraft?style=social)|免费|
|Stable Audio|stability.ai旗下的AI音乐、音效生成应用|[URL](https://www.stableaudio.com/)|免费/付费|
|OptimizerAI|音效生成|[URL](https://www.optimizerai.xyz/) [官方推文介绍](https://twitter.com/OptimizerAI/status/1779881263358419243)|免费/付费|

### AI视频创作
| 名称 | 说明 | 链接 | 费用 | 
| ---- | ----------------------------- | --- | --- | 
| 剪映 |字幕生成语音、识别语音、一键图文成片，还有很便捷、强大的视频剪辑功能|[URL](https://www.capcut.cn/)|免费/vip|
| 快手可灵|支持文生视频和图生视频|[URL](https://kling.kuaishou.com/)|免费|
| 即梦AI|字节跳动旗下的文生图、AI视频生成和AI图片编辑应用|[URL](https://jimeng.jianying.com/ai-tool/home)|免费/付费|
| Dream Machine|由 Luma AI 提供。Dream Machine 是一个人工智能模型，能根据文本和图像快速制作出高质量、逼真的视频。[官方介绍视频](https://www.youtube.com/watch?v=Zb3tffmBPRE)|[URL](https://lumalabs.ai/dream-machine)|免费/付费|
| Sora | OpenAI的文本生成视频的模型。Sora技术报告：https://github.com/ikaijua/Awesome-AITools/discussions/54, Sora的访问权限未完全开放，部分视觉艺术家、设计师和电影制作人获得了访问权限 | [URL](https://openai.com/sora) | - |
| Runway | Gen-2: 文本/图像 AI生成视频 <br> Gen-1: 根据视频AI生成视频 <br>应用示例：<br> [B站视频：数字生命卡兹克/我用AI做了一部《流浪地球3》的预告片](https://www.bilibili.com/video/BV1hF411f7rg) | [URL](https://runwayml.com/) | 付费/有一定的免费试用额度|
| Pika | 文本/图像 AI生成视频| [URL](https://pika.art/home)|	Paid/Free trial付费/有一定的免费试用额度|
| Fliki | 將文字生成音频和视频的网站 | [URL](https://fliki.ai) | 免费/付费 |
| d-id | 根据文字生成数字人的配音视频 | [URL](https://studio.d-id.com) | 付费，有一定的免费试用额度 |
| HeyGen | 根据文字生成数字人的配音视频 | [URL](https://app.heygen.com/) | 付费，有一定的免费试用额度 |
| AnimateDiff | Animatediff是香港中文大学团队开源的AI视频生成方法，基于Stable DIffusion的开源基建，8月份开源模型之后，一个月就把AI视频生成的质量提高了几个等级。<br>介绍文章：[这款工具让你一秒成AI版宫崎骏，AI视频“ChatGPT时刻”快到了](https://mp.weixin.qq.com/s/NgYv6VBSBRIBOFuyUnMnxA)| [Github](https://github.com/guoyww/AnimateDiff) ![GitHub Repo stars](https://img.shields.io/github/stars/guoyww/AnimateDiff?style=social)|免费|
|vivago.ai/video|	文本/图像生成视频; 4K视频增强|[URL](https://vivago.ai/video)|	免费|

### 学术科研
| 名称 | 说明 | 链接 | 费用 | 
| ---- | ----------------------------- | --- | --- | 
|gpt_academic|为GPT/GLM提供图形交互界面，特别优化论文阅读润色体验，模块化设计支持自定义快捷按钮&函数插件，支持代码块表格显示，Tex公式双显示，新增Python和C++项目剖析&自译解功能，PDF/LaTex论文翻译&总结功能，支持并行问询多种LLM模型，支持清华chatglm等本地模型。兼容llama,rwkv,盘古大模型等。|[GitHub](https://github.com/binary-husky/gpt_academic) ![GitHub Repo stars](https://img.shields.io/github/stars/binary-husky/gpt_academic?style=social)|免费|

### OCR图像识别文字
| 名称 | 说明 | 链接 | 费用 | 
| ---- | ----------------------------- | --- | --- |
|微信|微信对话框中的图片有提取文字的选项，识别效果很好，使用了几次基本没有什么识别错误。<br> [2021-03月份 微信AI对OCR功能的介绍：三年磨一剑——微信OCR图片文字提取](https://mp.weixin.qq.com/s/8Odh9TKKoxIYDpr1h-5Y5Q)||免费|
|Umi-OCR|开源、免费的离线OCR软件。支持截屏/粘贴/批量导入图片，段落排版/排除水印，扫描/生成二维码。内置多国语言库。|[Github](https://github.com/hiroi-sora/Umi-OCR) ![GitHub Repo stars](https://img.shields.io/github/stars/hiroi-sora/Umi-OCR?style=social)|免费|

### 视频内容总结
| 名称 | 说明 | 链接 | 费用 | 
| ---- | ----------------------------- | --- | --- |
| ChatGPT for YouTube | Chrome 插件，快速总结 Youtube 视频內容，需要登录chatgpt账号或者apikey | [URL](https://chatgpt4youtube.com/)| 免费 |
| Chat Youtube | 给一个Youtube 链接，它能给出总结，还可以向它提视频內容相关的问题 |[URL](https://chatyoutube.com) | 免费 |
| BibiGPT | 开源项目，音视频内容 AI 一键总结：哔哩哔哩、YouTube、网页、播客、会议、本地文件等| [GitHub](https://github.com/JimmyLv/BibiGPT) ![GitHub Repo stars](https://img.shields.io/github/stars/JimmyLv/BibiGPT?style=social)|免费|

### 人形机器人
| 名称 | 说明 | 链接 | 费用 | 
| ---- | ----------------------------- | --- | --- |
|Figure 01|获得了微软、OpenAI、英伟达和亚马逊等投资方的投资|[URL](https://www.figure.ai/)|
|Altlas|波士顿动力新的电动人形机器人|[URL](https://bostondynamics.com/atlas/)|
|Optimus Gen 2|特斯拉的人形机器人|[URL](https://www.youtube.com/watch?v=cpraXaw7dyc)|
|Apollo|Apptronik公司的人形机器人|[URL](https://apptronik.com/apollo)|
|GR-1|傅利叶公司的人形机器人|[URL](https://fourierintelligence.com/gr1/)|
|Digit|Agility公司的人形机器人|[URL](https://agilityrobotics.com/products/digit)|
|NEO|1x公司的人形机器人|[URL](https://www.1x.tech/androids/neo)|
|H1|宇树科技的人形机器人|[URL](https://www.unitree.com/h1/)|
|Phoenix|sanctuary.ai公司的人形机器人|[URL](https://sanctuary.ai/resources/news/sanctuary-ai-unveils-phoenix-a-humanoid-general-purpose-robot-designed-for-work/)|
|MenteeBot|以色列人形机器人公司 Meetee Robotics 发布的首款双足人形机器人|[URL](https://www.menteebot.com/)|

## 评测
### 大语言模型评测
- [B站视频：酷玩实验室/5大AI模型测评，带你一天上班摸鱼4小时！](https://www.bilibili.com/video/BV18841197Xa/), 2023-08-18
- [B站视频：【AI对决】让ChatGPT4出题！结果你绝对想不到！！](https://www.bilibili.com/video/BV1hT411W7YE/)
- [B站视频：阿里版GPT【通义千问】,和我的预期不一样](https://www.bilibili.com/video/BV1Va4y1T7Ym/)：
通义千问在自然科学和专业知识方面表现比较优秀，比如代码能力明显强于文心一言，甚至可以与chatgpt3.5掰掰手腕。在中文表达或者文学创作方面还有待提高，逊色于文心一言。
- [B站视频：chatgpt挑战知乎热门问题-GPT3.5 对战 GPT4](https://www.bilibili.com/video/BV1WM4y1a7a1/)

## 精选文章
### chatgpt相关文章
- [Sparks of Artificial General Intelligence:
Early experiments with GPT-4](https://arxiv.org/pdf/2303.12712v1.pdf): 该论文是一篇长达154页的对 GPT-4 的测试。微软的研究院在很早期就接触到了 GPT-4 的非多模态版本，并进行了详尽的测试。这篇论文不管是测试方法还是测试结论都非常精彩，强烈推荐看一遍。
- [《GPT-4 ，通用人工智能的火花》论文内容精选与翻译](https://orangeblog.notion.site/GPT-4-8fc50010291d47efb92cbbd668c8c893): [Sparks of Artificial General Intelligence:
Early experiments with GPT-4](https://arxiv.org/pdf/2303.12712v1.pdf) 这篇论文的精选和中文翻译。

## 其他
### Star 历史记录

[![Star 历史记录](https://api.star-history.com/svg?repos=ikaijua/Awesome-AITools&type=Date)](https://star-history.com/#ikaijua/Awesome-AITools&Date)


如果您喜欢这个项目，可以赞赏一下支持我们，谢谢您的支持！

<img src="https://github.com/ikaijua/Awesome-AITools/assets/126046795/76df3881-cf88-4767-96e0-157a2bb8f585" width="20%" height="20%" />   


