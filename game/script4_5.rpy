label game_if_battle_story:

    image overlay_14 = "33.14.png"
    show overlay_14 at truecenter with dissolve

    "地图缓缓展开。"
    "敌人大本营位于深处。"
    "此地严寒，不宜久留，应当速战速决。"
    n11 "原来如此，速度判定吗......"


    #第一问 选战术
    menu:
        "先观察敌军部署，再决定推进方式":
            $ tactic_choice = "observe"
            n11 "先看清楚地图。"
            n11 "如果这关真的是速度判定，那盲目强攻反而最浪费时间。"
            n2 "思路没错。"

        "集中兵力从正面强攻":
            $ tactic_choice = "frontal"
            n11 "正面主路最直接。"
            n11 "只要把中间打穿，应该就能最快推进。"
            n2 "最直接。"

        "先清扫外围敌军，稳步推进":
            $ tactic_choice = "steady"
            n11 "先把外围清掉比较稳。"
            n11 "这样后面推进的时候，也不会被拖住。"
            n2 "听起来起来“很稳”。"

    "迅速确认了当前的战场态势。"
    "下一步，就是决定真正的突破路线。"

    # 第二问 选路线
    menu:
        "走中央主路，直接切向敌军中枢":
            $ route_choice = "center"
            n11 "主路最短。"
            n11 "如果运气够好，直接从这里打穿就是最快的。"
            "但敌军的主力，也正密集地堆在这条线上。"

        "从左侧侧翼绕行，避开主力":
            $ route_choice = "left_flank"
            n11 "……左侧。"
            n11 "虽然看起来不是最直的一条路，但防线明显更薄。"
            n11 "如果目的是“最短时间到达本营”，这边反而更合理。"
            n2 "你抓到重点了。"

        "沿右侧据点推进，边打边压":
            $ route_choice = "right_push"
            n11 "右侧据点比较分散。"
            n11 "一边压过去，一边稳住局势，也许会更保险。"
            "可每一个据点，都意味着额外的停留和消耗。"

    "部队沿着选定的路线开始推进。"
    "最初的一切都还算顺利。"

    "然而很快，战场左侧传来了新的异动。"

    "昔日友人，再一次挡在了面前。"

    n11 "又来？"
    n2 "他有点烦了，对吧。"
    n11 "嗯......但是他有点像我弟弟......怎么说呢......"
    n2 "叛逆期？"
    n11 "对，叛逆期。"
    n11 "虽然听医生说他最近过得还不错，但是还是不乐意见我啊......"
    n2 "下次一起去看他吧，强行看望。"
    n11 "......"
    n11 "好。"

    #第三个可以问啥......我干嘛要为难自己......
    menu:
        "停下来，先解决眼前旧友":
            $ final_choice = "rush_camp"
            n11 "不能放着他不管。"
            n11 "这里仍然是最快的路径。"
            "停下脚步，转而处理眼前的敌人。"
            "局面被稳住了。"

        "无视纠缠，继续突进敌人大本营":
            $ final_choice = "support"
            n11 "现在停下来，才是真的来不及。"
            "压下动摇，命令部队更换路线。"
            "可惜别的路线敌人更多，推图的进度变慢了！"

        "暂时后撤，重新整理队形":
            $ final_choice = "retreat"
            n11 "先退一步，整理阵形。"
            n11 "这样至少不会在这里崩盘。"
            "可战场不会因为犹豫而停下来。"
            "敌军正在以前所未有的速度完成集结。"

    "最后的冲刺开始了。"

    if tactic_choice == "observe" and route_choice == "left_flank" and final_choice == "rush_camp":
        jump if_battle_success
    else:
        jump if_battle_fail


label if_battle_success:
    hide overlay_5
    hide overlay_4
    "npc" "精彩至极，各位表现远远超出我的预期。"

    "以最小的代价撕开了敌军防线。"
    "当部队冲进敌人大本营时，一切都还来得及。"

    n11 "很顺利啊。"

    "过了一会儿，屏幕上出现了四个大字。"
    hide overlay_14 with dissolve
    image overlay_15 = "33.15.png"
    show overlay_15 at truecenter with dissolve
    "没有像原本那样，在这里迎来注定的结局。"

    n2 "……你居然真的打出来了。"
    n2 "我试了好多次呢。"
    n11 "这么难吗？"
    $ baozi_score += 1
    n11 "......"
    n11 "感觉安心了。"
    n2 "毕竟是保住了朝夕相处的战友。"
    n11 "CG在杯子碎掉的那一刻我差点心梗了......"
    n11 "看到大家都赶来了就安心了。"

    jump after_if_battle


label if_battle_fail:

    "最终还是攻进了敌人大本营。"
    "只是，已经太晚了。"

    hide overlay_5
    hide overlay_4
    hide overlay_14 with dissolve
    image overlay_16 = "33.16.png"
    show overlay_16 at truecenter with dissolve
    "屏幕上的那个人倒在一片寂静里。"
    "酒杯摔碎的声音似乎在突出这一悲剧。"
    "所有台词都停在了最不该停下的地方。"

    n11 "......"

    scene bg room54_1
    $ wu_head_img = "images/1.png"
    $ guo_head_img = "images/2.png"
    n11 "感觉，有点失落。"
    n2 "正常，毕竟是朝夕相处的战友嘛......"
    n2 "而且历史上他确实在这之后不久就去世了。"
    n11 "哎，好可惜啊......"
    n2 "......"
    n2 "应该是今天运气不太好。"
    n2 "我的酒壶仙人也死掉了。"
    n11 "......"
    n11 "那有机会，一起去买别的吧。"
    n11 "买个更好养，更可爱的。"
    n11 "......"
    n11 "时间不早了，我该回去了。"
    n2 "哦，嗯，好，路上小心，下次再来玩。"
    n11 "好。"
    stop music fadeout 5.0
    scene bg room0
    "哎......"
    image bg room63 = "images/63.png"
    scene bg room63
    "下楼看见了有点眼熟的身影。"
    n11 "嗯？"
    n11 "貌似是隔壁班的......"
    n11 "他也住这里吗？"
    n11 "......"
    n11 "奉孝......"

    jump week7


label after_if_battle:
    $ wu_head_img = "images/1.2.png"
    $ guo_head_img = "images/2.1.png"

    #燥候虎子哥cg （收到图了 说实话 很失望 我一直在哭）
    scene bg room54_1 with dissolve

    "放下手柄，屏幕的光还停留在刚刚那一战的余温里。"
    #这个地方要来点暧昧的 啊 暧昧）能不能亲嘴啊
    n2 "真好啊......"
    n2 "不过就算失败了也没关系，还有下一个周目，或者是直接读档。"
    n11 "嗯，但是这样还是花了很多时间啊。"
    n11 "现在这样最好。"
    n2 "现实里可没有那么高的试错成本啊。"
    n11 "......"
    n11 "所以才要从一开始就把握住机会。"
    n11 "那么重要......一开始就要保护好，不是吗？"
    n11 "接下来，都是上坡路了，对吧？"
    n2 "......"
    n2 "对。"
    stop music
    play music music11
    show bg room54 at screen_shake
    pause 0.2
    show bg room54
    "“嗡————”"
    "“嗡————————”"
    stop music
    n11 "不接吗？"
    n2 "管他呢，忙着打游戏。"
    n2 "喂紫鸾，我的酒壶仙人重开了，现在还是婴儿时期，能不能帮我照顾一下。"
    n2 "我去弄点吃的，你今晚在这里过夜吧。"
    n11 "好。"

    scene bg room0
    "......"
    "很不巧的是，奉孝的厨艺真的太糟糕了。"
    "最终还是决定出门找吃的。"
    "......"
    "干脆我精进一下厨艺，之后邀请他来吃吧。"




    jump week7
    return