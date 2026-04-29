# 来源依据与可追溯说明

访问日期：2026-04-29。来源可能更新；涉及学校、期刊或平台政策时，应以用户提交时的最新官方说明为准。

## Agent Skills 格式

- Agent Skills Specification, `https://agentskills.io/specification`  
  要点：skill 是包含 `SKILL.md` 的目录；frontmatter 至少包含 `name` 和 `description`；可包含 `scripts/`、`references/`、`assets/`；通过渐进披露按需加载。

- OpenAI Academy, Skills resource, `https://academy.openai.com/public/clubs/work-users-ynjqu/resources/skills`  
  要点：`SKILL.md` 是可复用工作流说明，通常包括输入、步骤、输出格式和最终检查；Skills 可导入/导出到支持 Agent Skills 格式的工具，包括 Codex。

- Claude custom skills documentation, `https://claude.com/docs/skills/how-to`  
  要点：技能目录名必须匹配 `SKILL.md` 的 `name`；Claude.ai 的 description 限制更短；ZIP 应包含技能目录本身，而不是把 `SKILL.md` 直接放在 ZIP 根目录。

## 检测方法研究

- Mitchell, E. et al. (2023). **DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature**. ICML/PMLR. `https://proceedings.mlr.press/v202/mitchell23a.html`  
  要点：利用生成文本在模型概率函数中的曲率特征做零样本检测。

- Gehrmann, S., Strobelt, H., & Rush, A. M. (2019). **GLTR: Statistical Detection and Visualization of Generated Text**. ACL Anthology. DOI: `10.18653/v1/P19-3019`, `https://aclanthology.org/P19-3019/`  
  要点：通过词的概率排名等统计信号辅助识别生成文本。

- Wu, J. et al. (2023/2024). **A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions**. arXiv: `2310.14724`, `https://arxiv.org/abs/2310.14724`  
  要点：检测方法包括水印、统计检测、神经分类器和人工辅助等，检测问题会随模型发展而变化。

- Liang, W. et al. (2023). **GPT detectors are biased against non-native English writers**. Patterns, 4(7), 100779. DOI: `10.1016/j.patter.2023.100779`, `https://www.sciencedirect.com/science/article/pii/S2666389923001307`  
  要点：检测器可能对非母语作者产生误判风险，说明检测结果不宜单独作为处分依据。

## 平台说明与报告样例

- CNKI AI 学术研究助手/知网 AIGC 检测公开说明，`https://www.cnkiai.com/`  
  要点：公开页面说明系统分析论文上下文，建议提交正文；非正文如标题、公式、图片、表格、参考文献等可能影响检测；AIGC 值与论文质量无关，结果提供线索而非判断标准，仅供参考；当前版本支持中英文内容检测。

- 万方数据 AIGC 检测报告样例，`https://www.paperisok.net/demo/aigc.pdf`  
  要点：样例报告包含送检字符数、疑似 AI 生成文本字符数、疑似 AI 生成文本占比；报告说明标注文本只表示具有 AI 生成文本的部分特征，不确定为 AI 生成，结果仅供参考。

- 维普论文检测系统 AIGC 报告样例，`https://www.cnweipu.com/demo/aigc.pdf`  
  要点：样例报告末尾说明报告为算法自动生成，仅对所选择比对资源范围内检验结果负责，仅供参考。

- Turnitin AI writing detection model guide, `https://guides.turnitin.com/hc/en-us/articles/28294949544717-AI-writing-detection-model`  
  要点：Turnitin AI 检测模型持续更新；报告区分 AI-generated only、AI-paraphrased 等类别；1%-19% 低分区间可能以 `*%` 显示以降低误报风险；官方提醒 AI score 不应作为不利行动的唯一依据。

## 学术出版与披露边界

- 中国科学技术信息研究所等，《学术出版中 AIGC 使用边界指南 3.0》，`https://research.bjmu.edu.cn/docs/2025-12/45af8e65b76e4b788dedcdd5d4d12e14.pdf`  
  要点：强调透明度和问责制；AIGC 可用于提高文本可读性、逻辑组织和语言润色，但不应替代研究人员撰写全文、解释数据或直接得出科学结论；使用 AIGC 应披露使用者、工具版本、时间、提示、涉及部分和修改记录；检测与识别结果应作为辅助判断依据，并警惕误报。

## 使用这些来源的方式

- 解释检测原理时优先引用研究文献和平台公开说明。
- 写披露与学术诚信说明时优先引用《学术出版中 AIGC 使用边界指南 3.0》和目标学校/期刊政策。
- 处理具体报告时优先采用报告中的字段定义，不用本文件强行覆盖平台原文。
