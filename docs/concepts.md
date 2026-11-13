# Phase 01: Agentic AI engineering foundations

A traditional application follows rules written by a programmer. An LLM application
uses a model to interpret or generate language; its outputs are probabilistic and
must be validated. An autonomous agent adds a goal, state, and a loop that selects
actions, calls tools, observes results, and adjusts its approach. A single model
response does not by itself make an agent.

The agent loop is **Goal -> Think -> Act -> Observe -> Decide next action -> Repeat**.
For example, an agent asked to prepare a student report can inspect available data,
call a validation tool, calculate grades, inspect errors, request corrections, and
finish once a valid report has been produced. It needs stopping conditions and
limits on actions, time, and cost. This project's student app follows explicit
Python rules; it demonstrates engineering foundations rather than calling an LLM.

| Component | Responsibility |
| --- | --- |
| LLM | Interpret requests and propose actions; outputs still require checks. |
| Goal | Specify the desired outcome and completion criteria. |
| Tools | Perform bounded actions such as reading JSON or calculating grades. |
| Memory | Retain relevant information across interactions. |
| State | Track the current step, inputs, pending actions, and intermediate results. |
| Environment | The files, services, users, and systems an agent interacts with. |
| Feedback | Tool results, validation failures, and user corrections that guide the next step. |

Reliability requires validation, exception handling, and tests because model and tool
calls can fail. Security requires least privilege, protected secrets, and treating
external text as data rather than trusted instructions. Observability uses logs and
metrics to explain actions without exposing private data. Cost and latency need
budgets, caching where suitable, and limits on retries and tool calls. Scalability
requires managing concurrency and resource limits. Maintainability comes from
separate responsibilities, clear interfaces, and documentation. Governance requires
accountability, audit records, and human approval for consequential actions.

For the lab: explain these ideas in your own words and demonstrate a valid report,
an invalid marks rejection, the logs, the grade boundary tests, and the Git graph.
