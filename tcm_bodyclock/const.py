"""Constants for TCM Body Clock integration."""
from typing import Final

DOMAIN: Final = "tcm_bodyclock"

# 时辰名称、时间范围、经络值班、养生重点、推荐事项、注意事项
TCM_HOURS = [
    {"name": "子时", "start": 23, "end": 1, "meridian": "胆经值班", "health_tip": "阳气初生宜安眠", "recommend": "关闭电子设备，准备入睡", "avoid": "熬夜加班、刷手机"},
    {"name": "丑时", "start": 1, "end": 3, "meridian": "肝经值班", "health_tip": "藏血排毒黄金期", "recommend": "保持深度睡眠", "avoid": "吃宵夜、处理工作消息"},
    {"name": "寅时", "start": 3, "end": 5, "meridian": "肺经值班", "health_tip": "静卧养气待晨光", "recommend": "使用加湿器保持湿润", "avoid": "焦虑工作辗转反侧"},
    {"name": "卯时", "start": 5, "end": 7, "meridian": "大肠经值班", "health_tip": "晨起排浊正当时", "recommend": "喝温水唤醒肠道", "avoid": "匆忙起床忽略排便"},
    {"name": "辰时", "start": 7, "end": 9, "meridian": "胃经值班", "health_tip": "滋养后天之本时", "recommend": "吃温热早餐", "avoid": "空腹喝咖啡"},
    {"name": "巳时", "start": 9, "end": 11, "meridian": "脾经值班", "health_tip": "运化营养效率高", "recommend": "每小时起身活动", "avoid": "久坐喝冰饮"},
    {"name": "午时", "start": 11, "end": 13, "meridian": "心经值班", "health_tip": "阴阳交替需静养", "recommend": "午休20分钟", "avoid": "边看电脑边吃饭"},
    {"name": "未时", "start": 13, "end": 15, "meridian": "小肠经值班", "health_tip": "畅通血管喝点水", "recommend": "设置喝水提醒", "avoid": "饿肚开会"},
    {"name": "申时", "start": 15, "end": 17, "meridian": "膀胱经值班", "health_tip": "代谢排毒效率高", "recommend": "站立办公走动", "avoid": "憋尿久坐"},
    {"name": "酉时", "start": 17, "end": 19, "meridian": "肾经值班", "health_tip": "贮藏精华固元气", "recommend": "清淡晚餐放松", "avoid": "应酬暴饮暴食"},
    {"name": "戌时", "start": 19, "end": 21, "meridian": "心包经值班", "health_tip": "舒缓情绪护心神", "recommend": "听音乐放松", "avoid": "带工作回家"},
    {"name": "亥时", "start": 21, "end": 23, "meridian": "三焦经值班", "health_tip": "通调百脉备入眠", "recommend": "泡脚热敷肩颈", "avoid": "刷手机"}
]