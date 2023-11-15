import time
import subprocess
from xiaopy import *
from cotc import COTC

subprocess.run(["su", "root"])

try:
    ui = xp.ui()
    yangmao = ui.boolValue("yangmao")
    huatian = ui.boolValue("huatian")
    shuaye = ui.boolValue("shuaye")
    region = ui.stringValue("region")
    level = int(ui.stringValue("level"))
    mode = 1
    map_name = ui.stringValue("map_name")
    round_per_recover = int(ui.stringValue("round_per_recover"))
    c = COTC(region)
except Exception as e:
    xp.toast(e)

def initialization_position():
    print("初始化位置为：无名小镇")
    c.open_worldmap()
    time.sleep(1)
    xp.tap(95, 160)
    time.sleep(0.2)
    c.tap_worldmap_plus()
    c.tap_worldmap_podunk()
    print("点击小镇")
    time.sleep(1)
    c.tap_worldmap_proceed()
    c.tap_until_black_screen(c.cst.general_ok_btn_coord)
    c.await_black_screen_transition()
    print("已进入无名小镇")
    time.sleep(2)

def haoyangmao():
    time.sleep(0.5)
    print("寻找可点击对象……")
    if not c.tap_sheep():
        print("长时间未找到可薅的羊毛。准备薅花田")
        return

    print("检查获取物品……")
    if not c.wait_item_obtain():
        print("点击对象有误，脚本结束。")
        return

    if c.check_fleece_obtain():
        print("--获取三毛--")
        xp.tap(640, 433)
        time.sleep(1)
    else:
        print("--获取失败--")
        c.restart_cotc()
    haoyangmao()

def haohuatian(level, mode):
    time.sleep(0.5)
    while True:
        if mode == 1:
            print("点击左侧花田采集点……")
            xp.tap(760, 350)
            if c.wait_item_obtain():
                break
        elif mode == 2:
            print("点击右侧花田采集点……")
            xp.tap(930, 350)
            if c.wait_item_obtain():
                break
        elif mode == 3:
            print("花田结束，退出脚本……")
            return
    mode += 1
    print("检查获取物品……")
    if not c.wait_item_obtain():
        print("点击对象有误.")
        return

    time.sleep(0.2)
    success = False

    if level == 2 and region == 'tw':
        if xp.matchColor("#F0ECE7", 725, 345, 1.0):
            print("--获取12/15/18/21秘技果实--")
            success = True
            time.sleep(1)
            xp.tap(645, 433)
            mode += 1
    if level == 3 and region == 'tw':
        if xp.matchColor("#F0ECE7", 726, 345, 1.0):
            print("--获取24秘技果实--")
            success = True
            time.sleep(1)
            xp.tap(645, 433)
            mode += 1
    elif level == 4 and region == 'en':
        if xp.matchColor("#F0ECE7", 720, 340, 1.0):
            print("--获取30秘技果实--")
            success = True
            time.sleep(1)
            xp.tap(645, 433)
            mode += 1

    if success and mode == 3:
        print("--花田结束--")
        return
    if success and mode ==2:
        print("--左侧结束--")
        time.sleep(1)
        c.tap_minimap()
        time.sleep(1)
        c.tap_huatian_minimap()
        c.wait_main_screen_idling()
    else:
        print("--获取失败--")
        c.restart_cotc()
    haohuatian(level, mode)

battle_sequence = [
    # 第1回合
    {
        'skill_list': [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 1, 0, 0],
        ],
        'all_boost': True,
    }
]

battle_sequence_cait = [
    # 第1回合
    {
        'skill_list': [
            [-1, 1, 0, 0],
            [-1, 1, 0, 0],
            [-1, 1, 0, 0],
            [-1, 1, 0, 0],
        ],
        'all_boost': True,
    },
    {
        'skill_list': [
            [10, 1, 0, 0],
            [10, 1, 0, 0],
            [10, 1, 0, 0],
            [10, 1, 0, 0],
        ],
        'all_boost': True,
    }
]


def find_lv70_cat():
    ret = xp.findColor("#AE2C45", "1|1|#232327", 147, 60, 149, 62)
    if ret:
        return True
    else:
        return False


def find_lv55_cat():
    ret = xp.findColor("#000049", "1|0|#DBFFFF", 149, 69, 151, 70)
    if ret:
        return True
    else:
        return False


def find_lv50_cat():
    # ret = xp.findColor("#C0A048", "0|1|#7F672E", 157, 56, 158, 58)
    ret = xp.findColor("#112222", "1|0|#EFCDBB", 141, 68, 143, 69)  # 70武器
    if ret:
        return True
    else:
        return False

def run_script_battle():
    mc = c.cst.map_const[map_name]
    init_mode = mc['init_mode'] if 'init_mode' in mc else 1
    town_cat = mc['town_cat'] if 'town_cat' in mc else None
    wild_cat = mc['wild_cat'] if 'wild_cat' in mc else None
    total_recover_inn = 0
    c.open_worldmap()
    c.tap_worldmap_plus()
    if map_name == 'hell-white-grape-hill-path':
        c.tap_until_town_menu_opened([342, 342])
    if map_name == 'hell-castle-edoras' or map_name == 'hell-geist-canyon':
        c.tap_until_town_menu_opened([220, 550])
    time.sleep(0.5)
    c.tap_worldmap_proceed()
    c.tap_until_black_screen(c.cst.general_ok_btn_coord)
    c.await_black_screen_transition()
    print("进入旅店")
    c.tap_inn_on_main_screen(mc['rest_town'])
    c.await_black_screen_transition()
    time.sleep(2)
    print("点击旅店老板")
    c.recover_in_inn(mc['rest_town'])
    time.sleep(1)
    while True:
        total_encounter_count = 0
        common_encounter_count = 0
        cait_encounter_count = 0
        c.move_using_worldmap(mc['wild_coord'], wild_cat)
        c.await_black_screen_transition()
        while True:
            if total_encounter_count == 0 and init_mode >= 1:
                for index, init_obj in enumerate(mc['init_arr']):
                    # xp.log("93")
                    c.move_using_minimap(init_obj['init_coord'])
                    time.sleep(init_obj['init_idle'])
                    if index + 1 < len(mc['init_arr']):
                        c.await_black_screen_transition()
            elif common_encounter_count >= round_per_recover:
                break
            elif total_encounter_count % 4 == 0 and init_mode >= 2:
                init_obj = mc['init_arr'][-1]
                time.sleep(1)
                c.reset_minimap_show()
                c.move_using_minimap(init_obj['init_coord'])
                time.sleep(init_obj['init_idle'])
            # print("滑动遇敌")
            c.reset_minimap_show()
            c.swipe_until_black_screen([1000, 700], [1200, 700])
            c.wait_battle_idling()
            time.sleep(0.5)

            # if find_lv55_cat() or find_lv50_cat():
            #     c.flee_battle()
                # return
            if find_lv70_cat():
                c.run_preset_battle_sequence(battle_sequence_cait)
                cait_encounter_count += 1
                # print("抓猫第: " + str(cait_encounter_count) + "次。")
                # return
            # if find_lv55_cat():
            #     return
            else:
                # c.flee_battle()
                c.run_preset_battle_sequence(battle_sequence)
                common_encounter_count += 1
            # print("检测主界面")
            c.tap_until_main_screen_idling(c.cst.screen_center_coord)
            total_encounter_count += 1
            # print("战斗第: " + str(total_encounter_count) + "次。")

        c.move_using_worldmap(mc['town_coord'], town_cat)
        # xp.toast("移动到村庄")
        c.await_black_screen_transition()
        # xp.toast("进入旅店")
        c.tap_inn_on_main_screen(mc['rest_town'])
        c.await_black_screen_transition()
        time.sleep(2)
        # xp.toast("点击旅店老板")
        c.recover_in_inn(mc['rest_town'])
        time.sleep(1)
        total_recover_inn += 1
        xp.toast("旅店恢复: " + str(total_recover_inn) + "次。")
        if total_recover_inn % 20 == 0:
            c.restart_cotc()
            time.sleep(1)


def run_script():
    initialization_position()
    if yangmao:
        print("正在移动到羊圈...")
        c.tap_minimap()
        time.sleep(1)
        c.tap_yangjuan_minimap()
        c.wait_main_screen_idling()
        haoyangmao()
        print("薅羊毛结束。")
        time.sleep(5)
    if huatian:
        print("正在移动到花田...")
        c.tap_minimap()
        time.sleep(1)
        c.tap_huatian_minimap()
        c.wait_main_screen_idling()
        haohuatian(level, 1)
        print("薅花田结束。")
        time.sleep(5)
    if shuaye:
        print("正在移动到刷野地图...")
        run_script_battle()

run_script()
