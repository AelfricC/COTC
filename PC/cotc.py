import time
import subprocess
from xiaopy import *
from importlib import import_module

#   开发者参数部分 - 通过调整参数改变脚本性能
stability_mode = 0
turn_on_in_game_log = False
turn_on_console_log = False


#   -------------------------------------------------------------------------------------------------
#   -------------------------------------------------------------------------------------------------
#   底层方法部分 - 底层操作，对小派API再封装以实现某些特殊效果。
#   -------------------------------------------------------------------------------------------------
#   -------------------------------------------------------------------------------------------------
def log(text):
    if turn_on_in_game_log:
        xp.log(text)
    if turn_on_console_log:
        print(text)


def wait(t):
    _t = t + 0.2 * stability_mode
    # log("等待：" + str(_t) + "秒")
    time.sleep(_t)


def tap(x, y):
    _t = 0.05 + 0.02 * stability_mode
    # log("点击：" + str(x) + ", " + str(y))
    xp.tap(x, y, _t)
    time.sleep(_t + 0.01)


def tap_preset_coord(coord):
    tap(coord[0], coord[1])


def check_statement(statement):
    return xp.findColor(statement[0], statement[1], statement[2][0], statement[2][1], statement[2][2], statement[2][3])


def tap_preset_coord_with_checking(coord, statement, check_per_turn=5, interval=0.10, inverted=False):
    while True:
        tap_preset_coord(coord)
        for i in range(check_per_turn):
            wait(interval)
            if not inverted and check_statement(statement):
                return True
            if inverted and not check_statement(statement):
                return True


def tap_found_coord_with_checking(statement, max_turns=-1, interval=0.10):
    t = 0
    while True:
        wait(interval)
        t += 1
        found_coord = check_statement(statement)
        # print(found_coord)
        if found_coord:
            tap(found_coord.x, found_coord.y)
            return True
        if t == max_turns:
            return False


def wait_with_checking(statement, max_turns=-1, interval=0.10, inverted=False):
    t = 0
    while True:
        wait(interval)
        t += 1
        if not inverted and check_statement(statement):
            return True
        if inverted and not check_statement(statement):
            return True
        if t == max_turns:
            return False


def tap_skill(boost, x1, y1, x2=0, y2=0):
    delay = 0.08 if boost == 1 else 0.15 + 0.02 * (boost - 1)
    xp.tap(x1, y1, delay)
    time.sleep(delay - 0.08)
    if x2 != 0 and y2 != 0:
        tap(x2, y2)


class COTC:
    def __init__(self, server):
        ret = xp.screenSize()
        if not (ret.width == 1280 and ret.height == 720):
            raise Exception("暂不支持的设备分辨率：" + str(ret.width) + 'x' + str(ret.height))

        if server == 'tw':
            self.package_name = 'com.boltrend.octopath.tc'
            # self.activity = 'com.epicgames.ue4.GameActivity'
            self.activity = 'com.epicgames.ue4.SplashActivity'
        elif server == 'en':
            self.package_name = 'com.square_enix.android_googleplay.octopathw'
            self.activity = 'com.epicgames.ue4.SplashActivity'
        else:
            raise Exception("暂不支持的服务器："+server)

        module = import_module('cotc_constants_1280x720')
        classes = getattr(module, 'COTCConstants')
        self.cst = classes(server)
        self.ser = server
        self.swipe_flip = 0
        xp.launchApp(self.package_name, self.activity)

    #   -------------------------------------------------------------------------------------------------
    #   -------------------------------------------------------------------------------------------------
    #   单元模块部分
    #   -------------------------------------------------------------------------------------------------
    #   -------------------------------------------------------------------------------------------------

    def swipe_preset_coord(self, coord1, coord2, duration):
        if self.swipe_flip == 0:
            self.swipe_flip = 1
            xp.swipe(coord1[0], coord1[1], coord2[0], coord2[1], duration)
            time.sleep(duration)
        elif self.swipe_flip == 1:
            self.swipe_flip = 2
            xp.swipe(coord2[0], coord2[1], coord1[0], coord1[1], duration)
            time.sleep(duration)
        elif self.swipe_flip == 2:
            self.swipe_flip = 3
            xp.swipe(coord2[0], coord2[1], coord1[0], coord1[1], duration)
            time.sleep(duration)
        elif self.swipe_flip == 3:
            self.swipe_flip = 0
            xp.swipe(coord1[0], coord1[1], coord2[0], coord2[1], duration)
            time.sleep(duration)

    def swipe_preset_coord_with_checking(self, coord1, coord2, statement, duration=0.3, check_per_turn=5, interval=0.10, inverted=False):
        while True:
            self.swipe_preset_coord(coord1, coord2, duration)
            for i in range(check_per_turn):
                wait(interval)
                if not inverted and check_statement(statement):
                    return True
                if inverted and not check_statement(statement):
                    return True

    def tap_skills_panel(self, n):
        # 检查技能面板是否开启需要注意，开局时漂浮移动的buff层级最高，会挡住技能面板，导致按键失效或判断错误
        return tap_preset_coord_with_checking(self.cst.skills_panel_coord[n], self.cst.battle_idling, inverted=True)

    def tap_switch_character(self):
        return tap_preset_coord_with_checking(self.cst.switch_character_coord, self.cst.switch_character_done, interval=0.15)

    def tap_memories_read(self):
        return tap_preset_coord_with_checking(self.cst.memories_read_btn_coord, self.cst.memories_confirm_read, check_per_turn=1)

    def tap_memories_ok_after_battle(self):
        return tap_preset_coord_with_checking(self.cst.memories_ok_btn_coord, self.cst.memories_read_exist, check_per_turn=1)

    def tap_until_ultimate_menu_shown(self):
        return tap_preset_coord_with_checking(self.cst.use_ultimate_coord, self.cst.ultimate_menu_opened, check_per_turn=2, interval=0.25)

    def tap_activate_ultimate(self):
        return tap_preset_coord_with_checking(self.cst.activate_ultimate_coord, self.cst.battle_idling, check_per_turn=2, interval=0.25)

    def tap_start_battle(self):
        return tap_preset_coord_with_checking(self.cst.start_battle_btn_coord, self.cst.battle_idling, check_per_turn=1, inverted=True)

    def tap_flee_battle(self):
        return tap_preset_coord_with_checking(self.cst.flee_battle_btn_coord, self.cst.battle_idling, check_per_turn=1, inverted=True)

    def tap_until_black_screen(self, coord):
        return tap_preset_coord_with_checking(coord, self.cst.black_screen_exist, check_per_turn=1)

    def swipe_until_black_screen(self, coord1, coord2, duration=0.3):
        return self.swipe_preset_coord_with_checking(coord1, coord2, self.cst.black_screen_exist_2, duration=duration, check_per_turn=1)

    def tap_until_minimap_show(self, coord, check_per_turn=1, interval=0.1):
        return tap_preset_coord_with_checking(coord, self.cst.minimap_exist, check_per_turn=check_per_turn, interval=interval)

    def tap_until_main_screen_idling(self, coord, check_per_turn=1, interval=0.1):
        return tap_preset_coord_with_checking(coord, self.cst.menu_exist, check_per_turn=check_per_turn, interval=interval)

    def tap_until_unreal_shown(self, coord, check_per_turn=1, interval=0.1):
        return tap_preset_coord_with_checking(coord, self.cst.unreal_shown, check_per_turn=check_per_turn, interval=interval)

    def tap_dialog(self):
        return tap_found_coord_with_checking(self.cst.dialog_exist, interval=0.2)

    def tap_menu(self):
        return tap_preset_coord_with_checking(self.cst.menu_btn_coord, self.cst.menu_clicked, check_per_turn=10, interval=0.2)

    def tap_menu_others(self):
        return tap_preset_coord_with_checking(self.cst.menu_others_btn_coord, self.cst.menu_opened, check_per_turn=10, interval=0.2)

    def tap_switch_account(self):
        return tap_preset_coord_with_checking(self.cst.switch_account_btn_coord, self.cst.account_menu_opened, check_per_turn=10, interval=0.2)

    def tap_switch_account2(self):
        return tap_preset_coord_with_checking(self.cst.switch_account_btn2_coord, self.cst.account_list_opened, check_per_turn=10, interval=0.2)

    def tap_switch_account_more(self):
        return tap_preset_coord_with_checking(self.cst.switch_account_more_coord, self.cst.account_list_opened, check_per_turn=10, interval=0.2, inverted=True)

    def tap_minimap(self):
        return tap_preset_coord_with_checking(self.cst.minimap_coord, self.cst.menu_exist, check_per_turn=1, inverted=True)

    def tap_worldmap(self):
        return tap_preset_coord_with_checking(self.cst.worldmap_btn_coord, self.cst.menu_exist, check_per_turn=2, interval=0.3, inverted=True)

    def tap_town_cat_world(self):
        return tap_preset_coord_with_checking(self.cst.town_cat_world_coord, self.cst.town_cat_world, check_per_turn=1, interval=0.2)

    def tap_town_cat_hell(self):
        return tap_preset_coord_with_checking(self.cst.town_cat_hell_coord, self.cst.town_cat_hell, check_per_turn=1, interval=0.2)

    def tap_party(self):
        return tap_preset_coord_with_checking(self.cst.party_btn_coord, self.cst.menu_opened, check_per_turn=1, interval=0.2)

    def tap_allies_list(self):
        return tap_preset_coord_with_checking(self.cst.allies_list_btn_coord, self.cst.allies_list_opened, check_per_turn=1, interval=0.2)

    def tap_until_town_menu_opened(self, coord):
        return tap_preset_coord_with_checking(coord, self.cst.town_menu_opened, check_per_turn=2, interval=0.5)

    def tap_worldmap_proceed(self):
        return tap_preset_coord_with_checking(self.cst.worldmap_proceed_btn_coord, self.cst.ok_move_exist, check_per_turn=1, interval=0.2)

    def tap_bt_npc(self, npc):
        return tap_found_coord_with_checking(self.cst.bt_npc_exist[npc], interval=0.2)

    def tap_inn_on_main_screen(self, town):
        return tap_found_coord_with_checking(self.cst.inn_exist[town], interval=0.2)

    def tap_inn_host(self, town):
        return tap_found_coord_with_checking(self.cst.inn_host_exist[town], interval=0.2)

    def tap_ally(self, ally):
        return tap_found_coord_with_checking(self.cst.bt_ally_exist[ally], interval=0.2)

    def tap_sheep(self):
        return tap_found_coord_with_checking(self.cst.sheep_exist, max_turns=15, interval=0.3)

    def tap_inquire(self):
        return tap_preset_coord_with_checking(self.cst.inquire_btn_coord, self.cst.inquire_menu_opened, check_per_turn=1, interval=0.2)

    def tap_impress(self):
        return tap_preset_coord_with_checking(self.cst.impress_btn_coord, self.cst.confirm_impress_exist, check_per_turn=1, interval=0.2)

    def tap_part_ways(self):
        return tap_preset_coord_with_checking(self.cst.part_ways_btn_coord, self.cst.ally_parting_ways, check_per_turn=1, interval=0.2)

    def tap_confirm_part_ways(self):
        return tap_preset_coord_with_checking(self.cst.general_ok_btn_coord, self.cst.ally_parting_ways, check_per_turn=1, interval=0.2, inverted=True)

    def tap_all_boost(self):
        return tap_preset_coord_with_checking(self.cst.all_boost_btn_coord, self.cst.character_all_boosted, check_per_turn=5, interval=0.1)

    def wait_skills_panel_shown(self):
        return wait_with_checking(self.cst.skills_panel_standby, max_turns=10)

    def wait_skills_panel_gone(self):
        return wait_with_checking(self.cst.skills_panel_standby, max_turns=20, interval=0.05, inverted=True)

    def wait_inquire_shown(self):
        return wait_with_checking(self.cst.inquire_exist, max_turns=25, interval=0.2)

    def wait_battle_idling(self, interval=0.5):
        return wait_with_checking(self.cst.battle_idling, interval=interval)

    def wait_black_screen_start(self):
        return wait_with_checking(self.cst.black_screen_exist, interval=0.5)

    def wait_black_screen_end(self):
        return wait_with_checking(self.cst.black_screen_exist, interval=0.5, inverted=True)

    def wait_main_screen_idling(self):
        return wait_with_checking(self.cst.menu_exist, interval=0.2)

    def wait_init_screen_idling(self):
        return wait_with_checking(self.cst.init_screen_menu_shown, interval=0.2)

    def tap_until_init_screen_gone(self, coord):
        return tap_preset_coord_with_checking(coord, self.cst.init_screen_menu_shown, check_per_turn=2, interval=0.5, inverted=True)

    def wait_minimap_disappear(self):
        return wait_with_checking(self.cst.minimap_exist, interval=0.2, inverted=True)

    def wait_allies_list_btn_shown(self):
        return wait_with_checking(self.cst.allies_list_btn_exist, interval=0.2)

    def wait_item_obtain(self):
        return wait_with_checking(self.cst.item_obtained, max_turns=10, interval=0.3)

    def wait_init_screen_ready(self):
        return wait_with_checking(self.cst.init_screen_ready1, interval=0.1)

    def check_fleece_obtain(self):
        return wait_with_checking(self.cst.three_fleece_obtained, max_turns=1, interval=0.2)

    #   -------------------------------------------------------------------------------------------------
    #   -------------------------------------------------------------------------------------------------
    #   复合模块部分
    #   -------------------------------------------------------------------------------------------------
    #   -------------------------------------------------------------------------------------------------
    def open_skills_panel(self, n):
        count = 0
        while True:
            if count > 0:
                log("【注意】：技能面板没有打开，重试")
            self.tap_skills_panel(n)
            count += 1
            if self.wait_skills_panel_shown():
                return

    def await_black_screen_transition(self):
        self.wait_black_screen_start()
        self.wait_black_screen_end()

    def open_minimap(self):
        self.wait_main_screen_idling()
        self.tap_minimap()

    def open_worldmap(self):
        self.wait_main_screen_idling()
        self.tap_worldmap()

    def open_party(self):
        self.wait_main_screen_idling()
        self.tap_party()

    def open_allies_list(self):
        self.wait_allies_list_btn_shown()
        self.tap_allies_list()

    def part_ways_ally(self, ally):
        self.tap_ally(ally)
        self.tap_part_ways()
        self.tap_confirm_part_ways()
        self.tap_until_minimap_show(self.cst.close_menu_btn_coord)

    def move_using_minimap(self, coord):
        self.reset_minimap_show()
        self.open_minimap()
        wait(0.3)
        tap_preset_coord(coord)

    def move_using_worldmap(self, coord, cat=None):
        self.open_worldmap()
        if cat == 'world':
            self.tap_town_cat_world()
        elif cat == 'hell':
            self.tap_town_cat_hell()
        self.tap_until_town_menu_opened(coord)
        time.sleep(0.5)
        self.tap_worldmap_proceed()
        self.tap_until_black_screen(self.cst.general_ok_btn_coord)

    def use_skill(self, n, boost=1):
        if n == 5:
            self.use_ultimate_skill()
        else:
            skill_coord = self.cst.skills_coord[n][boost - 1]
            count = 0
            while True:
                if count > 0:
                    log("【注意】：重复点击技能")
                tap_skill(boost, skill_coord[0], skill_coord[1], skill_coord[2], skill_coord[3])
                count += 1
                if self.wait_skills_panel_gone():
                    return

    def use_ultimate_skill(self):
        self.tap_until_ultimate_menu_shown()
        self.tap_activate_ultimate()

    def inquire_and_impress_bt_npc(self, npc):
        while True:
            self.tap_bt_npc(npc)
            if self.wait_inquire_shown():
                break
        self.tap_inquire()
        self.tap_impress()
        self.tap_until_black_screen(self.cst.lower_ok_btn_coord)

    def recover_in_inn(self, town):
        self.wait_main_screen_idling()
        #   这里点击旅店老板有概率失效，如果失效，改成带检查重复点击的设计
        self.tap_inn_host(town)
        wait(2)
        self.wait_minimap_disappear()
        self.tap_until_black_screen(self.cst.lower_ok_btn_coord)
        self.await_black_screen_transition()
        self.tap_until_minimap_show(self.cst.center_ok_btn_coord)

    def flee_battle(self):
        self.wait_battle_idling()
        self.tap_flee_battle()

    def run_preset_character_action(self, n, action, retry=False):
        switch_character = action[0] > 9
        skill_to_use = action[0] % 10 if action[0] != -1 else -1
        boost_level = action[1]
        require_checking = False if boost_level == 1 else True

        if skill_to_use == -1:
            return
        self.open_skills_panel(n)
        if switch_character and not retry:
            self.tap_switch_character()
            self.wait_skills_panel_shown()
        self.use_skill(skill_to_use, boost_level)

        if not require_checking:
            return
        boost_level_applied = self.cst.attack_boost_level_applied if skill_to_use == 0 else self.cst.skill_boost_level_applied
        boost_level_check_result = wait_with_checking(boost_level_applied[n][str(boost_level)], max_turns=10)
        if not boost_level_check_result:
            log("【注意】：角色boost等级错误，重新使用技能")
            self.run_preset_character_action(n, action, True)

    def run_preset_turn_sequence(self, turn):
        all_boost = turn['all_boost']
        skill_list = turn['skill_list']

        self.wait_battle_idling()
        for n, character_action in enumerate(skill_list):
            character_action[1] = 1 if all_boost else character_action[1]
            self.run_preset_character_action(n, character_action)
        self.wait_battle_idling(0.1)
        self.tap_all_boost() if all_boost else None
        self.tap_start_battle()

    def run_preset_battle_sequence(self, sequence_list):
        for i, sequence in enumerate(sequence_list):
            # log("开始第" + str(i+1) + "回合")
            self.run_preset_turn_sequence(sequence)
        self.tap_until_black_screen(self.cst.screen_center_coord)

    def move_towards_bt_npc(self, npc):
        if npc == 'bt_axe':
            self.move_using_minimap(self.cst.valore_main_boulevard_coord)
            wait(8)
            self.await_black_screen_transition()
            self.move_using_minimap(self.cst.bt_npc_coord_on_minimap[npc])
            wait(5)
        elif npc == 'bt_bow':
            # 方法1：通过小地图
            # self.move_using_minimap(self.cst.emberglow_east_district_coord)
            # wait(15)
            # self.await_black_screen_transition()
            # self.move_using_minimap(self.cst.bt_npc_coord_on_minimap[npc])
            # wait(12)
            # 方法2：通过大地图
            self.move_using_worldmap(self.cst.emberglow_laboratory_coord)
            self.await_black_screen_transition()
            self.move_using_minimap(self.cst.emberglow_laboratory_to_town_coord)
            self.await_black_screen_transition()
            self.move_using_minimap(self.cst.bt_npc_coord_on_minimap[npc])
            wait(8)
        elif npc == 'bt_tome':
            self.move_using_minimap(self.cst.theatropolis_library_coord)
            wait(15)
            self.await_black_screen_transition()
        elif npc == 'bt_spear':
            self.move_using_minimap(self.cst.rippletide_residence_coord)
            wait(7)
            self.await_black_screen_transition()
        elif npc == 'bt_dagger':
            self.move_using_minimap(self.cst.cragspear_slums_coord)
            wait(17)
            self.await_black_screen_transition()
            self.move_using_minimap(self.cst.bt_npc_coord_on_minimap[npc])
            wait(9)
        elif npc == 'bt_staff':
            self.move_using_minimap(self.cst.bt_npc_coord_on_minimap[npc])
            wait(5)
        elif npc == 'bt_fan':
            self.move_using_minimap(self.cst.bt_npc_coord_on_minimap[npc])
            wait(6)
        elif npc == 'bt_blade':
            self.move_using_minimap(self.cst.bt_npc_coord_on_minimap[npc])
            wait(6)

    def ac_swipe_to_bottom(self):
        while True:
            time.sleep(0.2)
            if check_statement(self.cst.account_list_opened):
                break
            else:
                xp.swipe(680, 350, 680, 150, 0.1)

    def restart_cotc(self):
        subprocess.run(["su", "root", "am", "start", "-W", "-S", self.package_name + "/" + self.activity])
        time.sleep(2)
        # print("等待登录界面……")
        if self.ser == 'tw2':
            while True:
                time.sleep(0.2)
                # cotc_pid = subprocess.run(["su", "root", "pidof", self.package_name], capture_output=True).stdout.decode('ascii')
                # if not cotc_pid:
                #     print("重新启动游戏……")
                #     xp.launchApp(self.package_name, self.activity)
                #     time.sleep(2)
                if check_statement(self.cst.init_screen_ready1) or check_statement(self.cst.init_screen_ready2):
                    break
                else:
                    tap(self.cst.enter_coord_network_issue[0], self.cst.enter_coord_network_issue[1])
            # print("进入登录界面……")
            time.sleep(1.0)
            while True:
                time.sleep(0.2)
                if check_statement(self.cst.login_retry1):
                    print("认证失败1……")
                    tap(self.cst.login_retry1_coord[0], self.cst.login_retry1_coord[1])
                    print("等待登录界面……")
                    wait_with_checking(self.cst.init_screen_ready1, interval=0.1)
                    print("进入登录界面……")
                elif check_statement(self.cst.login_retry2):
                    print("认证失败2……")
                    tap(self.cst.login_retry2_coord[0], self.cst.login_retry2_coord[1])
                    print("等待登录界面……")
                    wait_with_checking(self.cst.init_screen_ready2, interval=0.1)
                    print("进入登录界面……")
                elif check_statement(self.cst.fast_login_exist):
                    print("快速登录……")
                    tap(self.cst.fast_login_coord[0], self.cst.fast_login_coord[1])
                    time.sleep(0.5)
                    tap(self.cst.fast_login_first_acc_coord[0], self.cst.fast_login_first_acc_coord[1])
                elif check_statement(self.cst.black_screen_exist):
                    print("认证成功……")
                    break
                else:
                    tap(self.cst.enter_coord_network_issue[0], self.cst.enter_coord_network_issue[1])
            # ("等待游戏主界面……")
            self.wait_main_screen_idling()
        elif self.ser == 'tw':
            # print("等待游戏加载……")
            # self.tap_until_init_screen_idling([10, 10])
            # time.sleep(0.5)
            # tap(10, 10)
            print("等待登录界面……")
            self.wait_init_screen_idling()
            time.sleep(1.0)
            print("等待登录界面结束……")
            self.tap_until_init_screen_gone([10, 10])
            print("等待游戏主界面……")
            self.wait_main_screen_idling()
        elif self.ser == 'en':
            while True:
                time.sleep(0.5)
                if check_statement(self.cst.menu_exist):
                    print("成功进入游戏界面")
                    return
                elif check_statement(self.cst.emu_forbidden):
                    print("违反安全策略32")
                    tap(902, 447)
                    self.restart_cotc()
                    return
                else:
                    tap(10, 10)
        else:
            self.tap_until_main_screen_idling([10, 10], interval=0.5)

    # Razor-1101    --检测小地图丢失后开关世界地图重置
    def reset_minimap_show(self):
        while True:
            if check_statement(self.cst.minimap_exist):
                break
            else:
                #print("小地图消失，尝试开关世界地图重试")
                self.open_worldmap()
                self.tap_until_main_screen_idling(self.cst.close_menu_btn_coord)

    def tap_yangjuan_minimap(self):
        tap_preset_coord(self.cst.yangmao_minimap_coord)

    def tap_huatian_minimap(self):
        tap_preset_coord(self.cst.huatian_minimap_coord)

    def wait_with_checking_battle_status(self):
        while True:
            wait(0.2)
            if self.wait_battle_idling():
                self.tap_all_change()
                self.tap_all_boost()
                self.tap_start_battle()
            elif self.wait_battle_ending():
                self.tap_until_black_screen(self.cst.screen_center_coord)

    def tap_all_change(self):
        return tap_preset_coord_with_checking(self.cst.all_change_coord, self.cst.battle_idling, check_per_turn=1, inverted=True)

    def tap_worldmap_plus(self):
        return tap_found_coord_with_checking(self.cst.worldmap_opened_plus_notexist, interval=0.5)

    def tap_worldmap_podunk(self):
        time.sleep(1)
        ret = xp.findImage("无名小镇.png", 0.8)
        time.sleep(0.5)
        return xp.tap(ret.x+40, ret.y-30)
