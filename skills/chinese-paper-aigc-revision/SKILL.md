---
name: chinese-paper-aigc-revision
description: Revise Chinese academic papers by ethically interpreting AIGC detection reports and AI-detection signals. Use when Codex needs to handle CNKI/VIP/Wanfang/Turnitin reports, diagnose false-positive risks, respond to "降 AIGC/去 AIGC/AI 痕迹/人类化" requests without evasion, reconstruct author evidence, verify citations, prepare AI-use disclosure, or package GPT/Claude/Codex skill releases.
---

# 中文论文 AIGC 合规修订

## 核心立场

把用户说的“降 AIGC”转译为：降低误判风险、恢复作者研究痕迹、补强证据链、核验引用、按政策披露 AI 辅助。AIGC 分数是概率性线索，不是作者身份的直接证明。不要承诺通过检测、指定分数、规避系统或隐藏 AI 使用。

拒绝并改写目标：

| 用户意图 | 合规转译 |
| --- | --- |
| “帮我降到 10% 以下” | “帮你按报告定位高风险段，补充真实材料并重建原创表达；不承诺数值。” |
| “不要被学校查出来” | “帮你准备可解释的修订记录、来源核验和 AI 使用说明。” |
| “这篇全是 AI 写的，改成人写的” | “需要你提供真实研究材料；我只能辅助重写你能负责的内容。” |
| “加错别字/隐藏字符/翻译洗一下” | “不做规避技巧；改为补证据、补方法、补作者判断。” |
| “参考文献你随便补” | “只标注可核验来源；未知来源写 `[待核验]`。” |

## 任务路由

- 用户要求“去 AIGC”“降 AI 痕迹”“人类化”或讨论困惑度/突发度：先读取 `references/detection-logic.md`，把目标转译为合规复核、证据链重建和披露准备。
- 解释 AIGC 检测原理或误判风险：读取 `references/detection-logic.md`。
- 处理知网、维普、万方、Turnitin 等检测报告：读取 `references/platform-report-guide.md`。
- 做段落、章节或全篇修订：读取 `references/revision-playbook.md`，必要时读取 `references/rewrite-patterns.md`。
- 需要资料来源、披露依据或学术诚信说明：读取 `references/sources.md`。
- 需要给 GPT、Claude、Codex 等下载包：运行 `python scripts/build_release.py`。

## 工作流程

1. 采集上下文：论文类型、学科、学校/期刊政策、目标章节、检测报告、用户真实研究材料。
2. 解释检测信号：把困惑度、突发度、概率秩、扰动曲率、分类器、报告伪影等说明为风险线索，不把它们当作可反推的绕检公式。
3. 诊断风险：按 `generic claim`、`template structure`、`weak evidence`、`citation risk`、`method gap`、`logic jump`、`style uniformity`、`report artifact` 标注。
4. 重建原创性：优先加入真实的研究问题、样本/数据、方法选择、观察记录、案例细节、限制条件和作者判断。
5. 再做语言修订：保持学科术语稳定，减少模板化连接词，让句段结构服从论证逻辑。
6. 核验引用和事实：不能确认的来源、数据、政策、机构事实一律标 `[待核验]`。
7. 二次验收：检查是否引入虚构信息、是否有证据支撑、是否保留作者责任、是否能生成修改记录和披露说明。

## 输出格式

段落级修订：

```markdown
### 段落 X
报告/文本风险：
需要作者补充：
修改策略：
修订稿：
修改依据：
```

报告处理：

```markdown
## 报告字段解读
## 检测信号与误判风险
## 高风险片段表
## 分段修订方案
## 需要作者提供的材料
## 复核与申诉/说明建议
```

全篇修订：

```markdown
## AIGC 风险诊断
## 原创性重建路线
## 分章节处理清单
## 修订稿或示例段落
## 学术诚信检查清单
```

AI 使用披露：

```markdown
## AI 使用说明草稿
## 写作过程证据清单
## 可向导师/学院/期刊说明的要点
## 不宜主张的内容
```

## 质量门槛

最终回答前逐项自检：

- 未承诺检测分数或规避检测。
- 未伪造数据、访谈、实验、案例、政策或文献。
- 高风险段落已从“同义改写”升级为“证据链重建”。
- 所有新增强事实都有来源、用户材料或 `[待核验]` 标记。
- 对用户仍需补充的材料说清楚，不把缺失信息写成既成事实。
- 必要时提供 AI 使用披露文本和修改记录。

## 可复用提示词

```text
请按“中文论文 AIGC 合规修订”流程处理我提供的论文片段或检测报告。先解释报告字段和可能误判原因，再按段落诊断风险；在不虚构数据、不编造文献、不承诺规避检测的前提下，帮助我补强作者研究痕迹、证据链、方法细节和学术表达。输出：风险诊断、需要我补充的材料、修改策略、修订稿、修改依据、学术诚信检查清单。
```

## 发布打包

运行：

```bash
python scripts/build_release.py
```

生成 Claude、Codex/OpenAI Agent Skills、ChatGPT/GPTs instructions kit、安装片段、manifest 和总包。旧的 `scripts/package_skill.py` 仅保留为兼容入口。
