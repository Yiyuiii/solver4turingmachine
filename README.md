<!--
 * @Author         : yiyuiii
 * @Date           : 2024-06-04 00:00:00
 * @LastEditors    : yiyuiii
 * @LastEditTime   : 2024-06-04 00:00:00
 * @Description    : None
 * @GitHub         : https://github.com/yiyuiii
-->

<!-- markdownlint-disable MD033 MD036 MD041 -->

# Solver for Turing Machine (Board Game)

<p align="center">
  <a href="https://raw.githubusercontent.com/Yiyuiii/nonebot-plugin-moegoe/master/LICENSE">
    <img src="https://img.shields.io/github/license/Yiyuiii/nonebot-plugin-moegoe.svg" alt="license">
  </a>
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">
</p>

This is a solver for the board game: Turing Machine. 

For personal usage, the codes are relatively simple in logic. Some validators are missing but the filling is quite easy.

## :rocket: Usage

Manually adjust codes in main.py, especially `Qs = [xx]` and `answers = [xx]`. 

**Outputs:** 
`answers = get_answers(Qs)` gives out the possible answers under Qs, 
`get_query(Qs, answers)` gives out the best query number, 
the expectation of success probability after 3 questions (i.e. score), 
the questions to be asked in various situations, 
and the possible answers left after 3 questions.

Note that after 1 round of questions, the proposed query number may not be the best, since the codes yet do not consider the relationship between query numbers.
However, this is sufficient for the vast majority of validator settings. 
