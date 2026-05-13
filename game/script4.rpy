label week5:
define music11 = "audio/手机震动.mp3"
image bg room54 = "images/54.png"
scene black with Dissolve(5.0)
scene black
define music15 = "audio/白息.mp3"
play music music15 fadein 3.0
"......"
"......"
scene bg room54
"week5"
"今天要干什么呢？"
menu:
    "去学校":
        pass
    "不去学校":
        jump week6

n2 "紫鸾没有回我消息啊......"
n2 "昨天就说让我别找他，没事吧......"
play music music11
show bg room54 at screen_shake
pause 0.2
show bg room54
n2 "......"
"“嗡————”"
n2 "电话？"
"接吗？"
menu:
    "接电话":
        pass
        stop music
    "不接电话":
        stop music
        n2 "......"
        n2 "不是紫鸾......"
        n2 "......"
        n2 "算了......"
        "......"
        jump week6

"？" "喂，奉孝？"
"？" "还以为你今天也不打算理我。"
"？" "今天不和那个转校生一起翘课？"
"？" "喂，你们不会吵架了吧？"
"？" "你和他上床了吗？"
"？" "要不下次叫上他一起？"
"？" "我看你挺喜欢他的。"
"？" "我不介意多人行。"
"？" "还是说你俩撞号了？"
"？" "那我可以再多叫一个人。"
n2 "......"
n2 "够了。"
n2 "我今天来。"
n2 "你别打扰他。"
"？" "好啊，等你来。"
n2 "......"
define music15 = "audio/白息.mp3"
play music music15 fadein 3.0
show bg room0
"不是我自嘲，我这个人不仅运气差，眼光也挺差。"
"我不是想讲什么原生家庭的痛什么的，这部分直接跳过。"
"我的意思是，在我懂事之后，在我发现我有能力掌握自己的命运之后，我周围的一切仍然很糟糕。"
" 我很早就意识到我比周围人聪明，而且相貌也出众，幽默风趣，为人和善。"
"可我周围都是一些烂人，也有可能是因为我本来就是个烂人。"
"情人节想给我告白的女孩确实排队到了校门口。"
"但是我眼光不好，选了最差的一个。"
"......"
"虽然事后在人家背后这么说别人坏话不好，但她确实很差劲。"
"没有说我是好人的意思。"
"总之我选了一个很差劲的女孩子，让我装得像大人一样，去酒吧喝酒。"
"结局就是她找上别的男人了，而我......"
image bg room55 = "images/55.png"
show bg room55 with dissolve
"......"
"发现了酒是好东西。"
"就是第二天起床头有点痛，肠胃也不舒服。"
"前一天？爽就完事。"
"过去所有的痛苦在那一晚上一笔勾销。"
"然后又喜提婴儿般的睡眠。"
"没有比这更让人快活的事了。"
"然后，在这之后？"
"我发现我的兴趣甚至不在于女人。"
image bg room57 = "images/57.png"
show bg room57 with dissolve
"有个女孩叫上了另外一个男人，于是我们三个人一起。"
"再准确来说，我被夹在中间了。"
"之后？"
"之后就没有女人的事了。"
"当躯壳的边界被彻底打破，性别的差异便显得毫无意义。"
"再之后？"
"明明只是一夜情，却有人趁热告白的。"
"我有些厌恶那些带有温度的情感博弈，于是全部都拒绝了。"
"偶尔会遇到那么些难缠的。"
"所以再之后......"
show bg room0
"在学校里寻觅几位各取所需的固定伴侣，按部就班地维系这种冰冷且稳定的放纵。"
"按照日期，一个一个来，我不太擅长对付很多人。"
"这是我的故事。"
"嗯？还在想我有什么悲惨的故事吗？"
"都是我自愿的。"
"都是我自找的。"
"我不是什么好人，当然也不算不良，至少表面上我还是那个优等生。"
"我以为这份稳定会持续很久。"
"直到......"
scene bg room6
$ wu_head_img = "images/1.png"
n11 "我是紫鸾。"
n11 "请多关照。"
show bg room0
"那是心脏被击中的感觉。"
"还有怀念的感觉。"
"直觉告诉我，我对他一见钟情了。"
"在死寂了许久之后，我的胸腔内传来了阵雨般的悸动，紧促得让人心慌。"
"想要了解他。"
"可是我这种人......"
scene bg room6
"老师" "那个......我看一下......新同学可以坐在......"
$ guo_head_img = "images/2.3.png"
n2 "老师，我旁边是空的。"
"我挥了挥手。"
show bg room0
"......"
"我这种人......"
"罢了，万一又是一时冲动呢？"
"和过去无数个一夜情一样的冲动。"

if baozi_score >= 7:
    pass
else:
    jump week6

"什么时候开始察觉到异样的呢？"
scene bg room22
"是在露天的走廊的时候吗？"
"发现他看向天空的眼神很有共鸣。"
"在那一瞬间就意识到某些方面我们是差不多的人。"
scene bg room15
"是在看樱花的时候吗？"
"对的，我注意到了......"
"他的家人其实已经不在了。"
"......"
"现在，还是别告诉他了。"
scene bg room18
"对，是在他邀请我的时候。"
"他快要知道真相了。"
"他一定会崩溃的。"
"只要有我在他身边......"
image bg room58 = "images/58.png"
scene bg room58
"这个时候谁在都可以，但是运气很好的是，他选的是我。"
"是我在他身边。"
scene bg room0
"再之后......"
scene bg room39
"他邀请我了......"
"就像我邀请其他人那样......"
"我应该没有拒绝的理由才对。"
"我不应该拒绝，不是吗？"
"这就是我想要的不是吗？"
"......"
scene bg room53
"搞砸了。"
"因为氛围正好。"
"我其实反应过来了。"
"我应该提前挡住他。"
"他就是受刺激了，需要一个人陪，没有那方面的意思。"
"我明知他此刻的索求只是源于精神崩塌后的应激反应，却依然贪婪地放任了那种温存。"
"我不仅是在趁虚而入，我是在亵渎他......"
"......"
scene bg room0
image bg room59 = "images/59.png"
image bg room60 = "images/60.png"
image bg room61 = "images/61.png"
"“喂，我说......”"
"？" "咋了？"
scene bg room61
"“我好像，坠入爱河了......”"
"？" "那可真是，可喜可贺了。"
"？" "谁，那个转校生？"
"“嗯。”"
"？" "那还真是恭喜了，那要和我们断联吗？"
"“不。”"
"？" "也是呢，毕竟你也不是什么好人。"
"“谢谢夸奖。”"
scene bg room60
"？" "反正你也只是男女通吃前后都可，看对眼了就找人上床的烂黄瓜，连后面都变成竖着的缝了。"
"？" "这个样子叫别人看到，肯定就把人吓跑了。"
"“确实啊。”"
"？" "看来你最近有点寂寞了啊，早喊你多来找我们几次呢。"
"？" "你胡思乱想太多了，我们可以一起去喝更多的酒，上更多次床，那个转校生和你做不了的事，我们可以和你做。"
"？" "他要是看到你现在这样，估计早就被吓跑了不是吗？"
"？" "其实你自己也清楚，这样是不对的。"
"？" "人类其实本质上都是孤独的，这种建立在新鲜感上的冲动，保质期短得可怜。"
"？" "你看，那个转校生现在也许正觉得生活美好，那是因为他还没见过你这副烂透了的样子。"
scene bg room59
"？" "一旦他发现你到底是个什么货色，那种眼神会让你比现在更寂寞。"
"？" "你会伤害他，他最终也会厌恶你，与其等到那天互相撕破脸皮，还不如打从一开始就别去祸害人家。"
"？" "你根本不是坠入爱河，你只是太缺爱、太寂寞了。"
"？" "这种廉价的错觉，不过是你滥情遗留的习惯性问题。"
"？" "别想太多了，只有我们现在的关系才是最真实、最稳固的，因为我们本来就都在地狱里。"
"？" "没关系，如果你还是觉得心里空落落的，我们可以再来几个回合。"
scene bg room0
"？" "我可以多叫几个人过来陪你，如果你真的那么舍不得那个转校生……"
"？" "只要你想，我甚至可以把他一并叫过来。"
"......"
"“不了，没必要给别人添麻烦，你也觉得麻烦不是吗？”"
"“你今天话有点密了，闭上嘴多来几个回合吧。”"
"？" "好好，今天必须让我们的公主殿下满意。"
stop music fadeout 10.0
"这样就好。"
"这样最好。"
"......"
scene bg room0 with Dissolve(5.0)


label week6:
define music16 = "audio/夜風の火花.mp3"
scene bg room0
"......"
"......"
scene bg room3
"week6"
"今天要干什么呢？"
menu:
    "出门":
        if baozi_score >= 7:
            pass
        else:
           jump week7
    "不出门":
        jump week7
    
play music music11
show bg room3 at screen_shake
pause 0.2
show bg room3
"“嗡————”"
stop music
n11 "啊，是奉孝啊。"
"在那天之后我去找他他一直躲着我，可他来联系我的时候我也一直在回避。"
"会不会做得有点太过分了......"
n11 "喂？"
"奉孝" "喂，紫鸾啊，还记得我之前给你说的游戏吗？"
"奉孝" "我打完了，要来我家玩吗？"
"想不出拒绝的理由"
n11 "好啊，你给个时间吧，我过来。"
"奉孝" "太好了，那明天下午我们翘课吧。"
"嗯。"
"......"
play music music11
show bg room3 at screen_shake
pause 0.2
show bg room3
"“嗡————”"
stop music
n11 "是谁啊？"
"陌生人消息？"
show bg room0 with dissolve
image bg room62 = "images/62.png"
show bg room62 with dissolve
"......"
"奉孝......"
"什么时候我也能......"
show bg room0 with dissolve
"......"

play music music16 fadein 3.0
scene bg room54
$ guo_head_img = "images/2.1.png"
n2 "欢迎来到奉孝之家。"
n2 "不用客气随便坐，游戏机那边还有懒人沙发。"
n2 "想要睡觉的话直接躺我床上就行，要喝饮料吗？"
n11 "水就行。"
n11 "......"
n11 "你家比我想象的整洁很多。"
n2 "在你印象里我是那种人吗？"
n11 "有一回打电话的时候，你被床边的东西绊倒。"
n11 "接着是一堆东西掉落的声音，还有易拉罐碰撞的声音。"
n11 "那天你出门的时候鼻子里还塞着纸团，该是脸着地了......"
n2 "停停，别揭我老底了，这是为了你来专门收拾过的好吧。"
n2 "不感动吗(ゝ∀･)"
$ wu_head_img = "images/1.1.png"
n11 "挺感动的。"
n11 "就是香水味道有点太重了，你喷了多少？"
n2 "嗯.....这个嘛......"
n2 "......"
n11 "你喜欢什么牌子的？"
n2 "嗯......看情况吧，有很多种不一样的......"
n11 "那有机会一起去买吧。"

image bg room54_1 = "images/54.1.png"

n2 "好......先不说这个，赶紧来玩这个游戏，很长的，一两天打不完的。"
n11 "行。"
"本来就准备慢慢玩的。"
n11 "那我玩的时候你干什么？"
n2 "看你玩。"
n2 "哦，还有，之前不是给你看过我的酒壶仙人吗？"
image overlay_3 = "33.2.png"
show overlay_3 at truecenter with dissolve
n2 "你看！"
n11 "......"
n11 "hp看起来有点岌岌可危了。"
n2 "对！就是这个！不知道为什么他看起来有一点死了！"
n2 "可能是我之前不小心摔了一下，也有可能是因为最近有点冷落他了。"
n11 "冷落什么的，你最近很忙吗？"
n2 "很忙啊。"
hide overlay_3
stop music fadeout 5.0
"他揉了一下我的脑袋。"
n2 "还有这么大一个活人需要多关照。"
$ wu_head_img = "images/1.2.png"
n11 "......"

define music17 = "audio/ショッピング_-_8bit.mp3"
play music music17 fadein 5.0
scene bg room0
n2 "那么，启动！"
image overlay_4 = "33.4.png"
show overlay_4 at truecenter with dissolve
$ wu_head_img = "images/1.6.png"
n11 "感觉，大制作啊。"
n11 "封面是主角吗？"
$ guo_head_img = "images/2.4.png"
n2 "对，他超帅的。"
n2 "而且超强。"
n2 "总之先过新手教程吧。"
n11 "好。"
image overlay_5 = "33.5.png"
show overlay_5 at truecenter with dissolve
"2 hours later......"
image overlay_6 = "33.6.png"
show overlay_6 at truecenter with dissolve
"“......本座乃大贤良师张角......向天下苍生展现了何为太平梦想......”"
n11 "......"
n11 "好可惜啊......"
n2 "怎么说？"
n11 "要是能有人更早一点阻止他误入歧途，他一定能助太平早点到来......"
hide overlay_6 with dissolve
show overlay_5 at truecenter with dissolve
"2 hours later......"
image overlay_7 = "33.7.png"
show overlay_7 at truecenter with dissolve
"“原来如此......”"
n11 "这家伙也......怪可惜的......"
n11 "可惜太极端了，怎么说都没办法回头了。"
n2 "若是换个时代，他也许有一统天下的才能呢。"
n2 "可惜，那离“太平”就很远了。"
hide overlay_7 with dissolve
show overlay_5 at truecenter with dissolve
"2 hours later......"
n2 "哦，关键的地方来咯，要选择要效忠的势力了。"
n11 "三选一啊......确实需要好好思考一下了。"
n2 "不要忘记存档哦~"
menu:
    "追随绿色的主公":
        jump week6_1
    "追随蓝色的主公":
        jump week6_2
    "追随红色的主公":
        jump week6_3

label week6_1:
image overlay_8 = "33.8.png"
show overlay_8 at truecenter with dissolve
n2 "你选择了他啊。"
n11 "他待人以诚，为人宽厚。"
n11 "尤其是他心系百姓，必然是好主公。"
n2 "不错不错。"
"就这样打了一天游戏。"
"度过了愉快的一天。"
jump week7

label week6_2:
image overlay_9 = "33.9.png"
show overlay_9 at truecenter with dissolve
n2 "好眼光，我也选择了他。"
n11 "怎么说呢......"
n11 "感觉吧，就是这边要厉害很多......"
n2 "大企业哦。"
n11 "大企业。"
n11 "同事也感觉很厉害。"
n2 "确实，各种各样的人才呢。"
n11 "军师也很多，感觉非常可靠。"
$ wu_head_img = "images/1.7.png"
n11 "啊，有新制服了。"
n2 "好耶，好帅啊(・w・)"
n11 "(｡•ㅅ•｡)"
hide overlay_9 with dissolve
show overlay_5 at truecenter with dissolve
"2 hours later......"
image overlay_11 = "33.11.png"
show overlay_11 at truecenter with dissolve
n11 "呼————"
n11 "好强啊，好难打。"
n11 "感觉在玩souls like。"
n2 "这才是真正的三国无双啊。"
n11 "还好大家都很给力，我才能打过。"
n11 "郭嘉大人真是帅啊。"
n2 "对对对。"
hide overlay_11 with dissolve
show overlay_5 at truecenter with dissolve
"2 hours later......"
image overlay_12 = "33.12.png"
show overlay_12 at truecenter with dissolve
n11 "......"
"屏幕上，像素的火焰在跳动，明明没有声音，我却觉得耳膜隐隐作响。"
n2 "抱歉，紫鸾，忘记提醒你这段剧情......"
"奉孝伸手过来，想要跳过这段剧情。"
n11 "......"
n11 "没事......"
n11 "我自己也忘了......"
n11 "但是没关系，之后会走上坡路的，对吧？"
n2 "......"
n2 "对。"
hide overlay_12 with dissolve
show overlay_5 at truecenter with dissolve
"2 hours later......"
image overlay_13 = "33.13.png"
show overlay_13 at truecenter with dissolve
n11 "主公真的不后悔吗......"
n2 "这是为了天下做出的，必要的牺牲罢了。"
n2 "道不同，不相为谋。"
n11 "昔日同伴，如今却是前进道路上必须铲除的障碍呢......"
n11 "......"
hide overlay_13 with dissolve
show overlay_5 at truecenter with dissolve
"2 hours later......"
n2 "要来了要来了，白狼山。"
n11 "很关键吗？"
n2 "嗯，打赢这场主公差不多就统一北方了。"
n2 "更重要的是，这里又有if线的分支剧情哦~"
n11 "......难道说......"
n2 "加油哦，难度还挺高的，记得存档。"
hide overlay_5
jump game_if_battle_story

label week6_3:
image overlay_10 = "33.10.png"
show overlay_10 at truecenter with dissolve
n2 "不错的选择。"
n11 "很喜欢这边的氛围啊。"
n11 "比起企业，更像是大家庭呢。"
n2 "确实呢，哥哥妹妹们还有长辈们都很好呢。"
n11 "这样的势力，想必以后掌权也能如此和睦吧。"
n2 "很好。"
"就这样打了一天游戏。"
"度过了愉快的一天。"
jump week7

hide overlay_5


return