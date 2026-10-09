# G021V plugins/ai/views/chat/index.vue：页面渲染、事件接线和生命周期

依赖：G000, G018, G019, G020, G021, G021F029, G021F033, G021F034, G021F035, G021F036, G021F037, G021F038, G021F039, G021F040, G021F042, G021F043, G021F044, G021F045, G021F046, G021F047, G021F048, G021F049, G021F050, G021F051, G021F052, G021F053, G021F054, G187, G231

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00183 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template lines 1-411（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00184 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 11: v-on:click
  - 基线：原表达式：clearChat；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00185 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 15: v-loading:
  - 基线：原表达式：sessionLoading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00186 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 17: v-for:
  - 基线：原表达式：session in sessionList；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00187 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 18: v-bind:key
  - 基线：原表达式：session.sessionId；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00188 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 19: v-bind:class
  - 基线：原表达式：[
              'session-item',
              currentSessionId === session.sessionId ? 'active' : '',
            ]；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00189 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 23: v-on:click
  - 基线：原表达式：loadSession(session.sessionId)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00190 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 41: v-on:click
  - 基线：原表达式：handleDeleteSession(session.sessionId)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00191 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 45: v-if:
  - 基线：原表达式：sessionList.length === 0 && !sessionLoading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00192 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 65: v-on:click
  - 基线：原表达式：openConfigDialog；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00193 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 69: v-model:
  - 基线：原表达式：currentModelId；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00194 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 75: v-for:
  - 基线：原表达式：item in modelOptions；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00195 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 76: v-bind:key
  - 基线：原表达式：item.modelId；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00196 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 77: v-bind:label
  - 基线：原表达式：`${item.provider}/${item.modelCode}`；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00197 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 78: v-bind:value
  - 基线：原表达式：item.modelId；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00198 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 84: v-on:scroll
  - 基线：原表达式：handleScroll；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00199 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 88: v-bind:class
  - 基线：原表达式：{ 'is-empty': messageList.length === 0 }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00200 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 90: v-if:
  - 基线：原表达式：messageList.length === 0；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00201 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 99: v-for:
  - 基线：原表达式：(msg, index) in messageList；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00202 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 100: v-bind:key
  - 基线：原表达式：index；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00203 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 101: v-bind:class
  - 基线：原表达式：[
                'message-row',
                msg.role === 'user' ? 'message-user' : 'message-ai',
              ]；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00204 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 108: v-bind:icon
  - 基线：原表达式：msg.role === 'user' ? 'UserFilled' : 'Service'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00205 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 109: v-bind:size
  - 基线：原表达式：40；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00206 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 110: v-bind:class
  - 基线：原表达式：msg.role === 'user' ? 'avatar-user' : 'avatar-ai'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00207 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 116: v-if:
  - 基线：原表达式：msg.createdAt；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00208 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 121: v-if:
  - 基线：原表达式：msg.role === 'user'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00209 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 123: v-if:
  - 基线：原表达式：msg.images && msg.images.length > 0；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00210 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 127: v-for:
  - 基线：原表达式：(img, idx) in msg.images；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00211 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 128: v-bind:key
  - 基线：原表达式：idx；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00212 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 129: v-bind:src
  - 基线：原表达式：getImageUrl(img)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00213 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 130: v-bind:preview-src-list
  - 基线：原表达式：msg.images.map(getImageUrl)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00214 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 138: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00215 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 139: v-bind:content
  - 基线：原表达式：msg.content；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00216 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 140: v-bind:reasoning-content
  - 基线：原表达式：msg.reasoningContent；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00217 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 141: v-bind:loading
  - 基线：原表达式：loading && index === messageList.length - 1；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00218 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 150: v-bind:icon
  - 基线：原表达式：DocumentCopy；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00219 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 152: v-on:click
  - 基线：原表达式：copyText(msg.content)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00220 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 156: v-if:
  - 基线：原表达式：
                        userConfig.metricsDefaultVisible == '0' &&
                        hasMetrics(msg)
                      ；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00221 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 163: v-if:
  - 基线：原表达式：
                          msg.metrics?.duration !== null &&
                          msg.metrics?.duration !== undefined
                        ；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00222 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 170: v-if:
  - 基线：原表达式：
                          msg.metrics?.inputTokens !== null &&
                          msg.metrics?.inputTokens !== undefined
                        ；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00223 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 177: v-if:
  - 基线：原表达式：
                          msg.metrics?.outputTokens !== null &&
                          msg.metrics?.outputTokens !== undefined
                        ；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00224 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 184: v-if:
  - 基线：原表达式：
                          msg.metrics?.totalTokens !== null &&
                          msg.metrics?.totalTokens !== undefined
                        ；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00225 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 191: v-if:
  - 基线：原表达式：
                          msg.metrics?.reasoningTokens !== null &&
                          msg.metrics?.reasoningTokens !== undefined
                        ；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00226 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 199: v-if:
  - 基线：原表达式：msg.role === 'assistant'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00227 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 204: v-if:
  - 基线：原表达式：currentSessionAgentData?.model；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00228 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 213: v-else-if:
  - 基线：原表达式：currentModelInfo；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00229 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 228: v-model:
  - 基线：原表达式：inputMessage；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00230 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 230: v-bind:rows
  - 基线：原表达式：3；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00231 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 233: v-on:keydown
  - 基线：原表达式：handleSend；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00232 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 234: v-bind:disabled
  - 基线：原表达式：loading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00233 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 238: v-if:
  - 基线：原表达式：userConfig.visionEnabled == '0' && inputImages.length；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00234 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 241: v-for:
  - 基线：原表达式：(img, idx) in inputImages；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00235 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 242: v-bind:key
  - 基线：原表达式：idx；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00236 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 243: v-bind:src
  - 基线：原表达式：getImageUrl(img)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00237 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 244: v-bind:preview-src-list
  - 基线：原表达式：inputImages.map(getImageUrl)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00238 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 252: v-if:
  - 基线：原表达式：
                    currentModelInfo &&
                    currentModelInfo.supportImages === 'Y' &&
                    userConfig.visionEnabled == '0'
                  ；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00239 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 263: v-bind:icon
  - 基线：原表达式：Picture；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00240 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 264: v-on:click
  - 基线：原表达式：triggerImageUpload；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00241 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 268: v-if:
  - 基线：原表达式：
                    currentModelInfo &&
                    currentModelInfo.supportReasoning === 'Y'
                  ；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00242 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 274: v-bind:type
  - 基线：原表达式：chatConfig.isReasoning ? 'primary' : ''；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00243 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 275: v-bind:plain
  - 基线：原表达式：!chatConfig.isReasoning；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00244 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 276: v-on:click
  - 基线：原表达式：chatConfig.isReasoning = !chatConfig.isReasoning；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00245 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 278: v-slot:icon
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00246 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 285: v-bind:type
  - 基线：原表达式：loading ? 'danger' : 'primary'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00247 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 286: v-bind:icon
  - 基线：原表达式：loading ? 'VideoPause' : 'Promotion'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00248 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 287: v-on:click
  - 基线：原表达式：handleMainAction；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00249 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 288: v-bind:disabled
  - 基线：原表达式：
                  !loading && !inputMessage.trim() && !inputImages.length
                ；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00250 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 302: v-model:
  - 基线：原表达式：showConfigDialog；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00251 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 308: v-bind:model
  - 基线：原表达式：editingUserConfig；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00252 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 309: v-bind:gutter
  - 基线：原表达式：20；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00253 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 310: v-bind:span
  - 基线：原表达式：12；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00254 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 313: v-model:
  - 基线：原表达式：editingUserConfig.temperature；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00255 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 314: v-bind:min
  - 基线：原表达式：0；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00256 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 315: v-bind:max
  - 基线：原表达式：2；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00257 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 316: v-bind:step
  - 基线：原表达式：0.1；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00258 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 317: v-bind:precision
  - 基线：原表达式：1；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00259 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 323: v-bind:span
  - 基线：原表达式：12；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00260 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 328: v-model:
  - 基线：原表达式：editingUserConfig.addHistoryToContext；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00261 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 332: v-bind:span
  - 基线：原表达式：12；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00262 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 335: v-if:
  - 基线：原表达式：editingUserConfig.addHistoryToContext == '0'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00263 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 338: v-model:
  - 基线：原表达式：editingUserConfig.numHistoryRuns；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00264 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 339: v-bind:min
  - 基线：原表达式：1；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00265 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 340: v-bind:max
  - 基线：原表达式：20；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00266 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 346: v-bind:span
  - 基线：原表达式：12；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00267 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 351: v-model:
  - 基线：原表达式：editingUserConfig.metricsDefaultVisible；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00268 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 355: v-bind:span
  - 基线：原表达式：12；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00269 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 360: v-model:
  - 基线：原表达式：editingUserConfig.visionEnabled；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00270 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 364: v-bind:span
  - 基线：原表达式：12；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00271 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 367: v-if:
  - 基线：原表达式：editingUserConfig.visionEnabled；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00272 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 370: v-model:
  - 基线：原表达式：editingUserConfig.imageMaxSizeMb；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00273 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 371: v-bind:min
  - 基线：原表达式：1；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00274 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 372: v-bind:max
  - 基线：原表达式：50；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00275 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 376: v-slot:suffix
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00276 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 382: v-bind:span
  - 基线：原表达式：24；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00277 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 385: v-model:
  - 基线：原表达式：editingUserConfig.systemPrompt；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00278 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 387: v-bind:rows
  - 基线：原表达式：4；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00279 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 394: v-slot:footer
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00280 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 396: v-on:click
  - 基线：原表达式：showConfigDialog = false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00281 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 397: v-on:click
  - 基线：原表达式：handleSaveConfig；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00282 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 402: v-if:
  - 基线：原表达式：userConfig.visionEnabled；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00283 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template line 408: v-on:change
  - 基线：原表达式：handleImageInputChange；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00284 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template interpolation line 30
  - 基线：原显示表达式：session.sessionTitle || "新对话"
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00285 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template interpolation line 33
  - 基线：原显示表达式：formatTime(session.createdAt)
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00286 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template interpolation line 115
  - 基线：原显示表达式：msg.role === "user" ? "我" : "AI 助手"
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00287 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template interpolation line 116
  - 基线：原显示表达式：formatTime(msg.createdAt)
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00288 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template interpolation line 135
  - 基线：原显示表达式：msg.content
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00289 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template interpolation line 167
  - 基线：原显示表达式：msg.metrics.duration.toFixed(3)
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00290 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template interpolation line 174
  - 基线：原显示表达式：msg.metrics.inputTokens
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00291 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template interpolation line 181
  - 基线：原显示表达式：msg.metrics.outputTokens
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00292 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template interpolation line 188
  - 基线：原显示表达式：msg.metrics.totalTokens
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00293 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template interpolation line 195
  - 基线：原显示表达式：msg.metrics.reasoningTokens
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00294 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template interpolation line 206
  - 基线：原显示表达式：currentSessionAgentData.model.provider
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00295 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template interpolation line 207
  - 基线：原显示表达式：currentSessionAgentData.model.id
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00296 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template interpolation line 215
  - 基线：原显示表达式：currentModelInfo.provider
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00297 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template interpolation line 216
  - 基线：原显示表达式：currentModelInfo.modelCode
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00298 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` template interpolation line 292
  - 基线：原显示表达式：loading ? "停止" : "发送"
  - 去向：react-front/plugins/ai/views/chat/index.tsx
- I00299 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` style[0] lines 902-1338
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/plugins/ai/views/chat/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
