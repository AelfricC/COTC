# COTC
new town location
L188
find cood from namelss town location

if a new town, get inn location and inn host location
L198
c.tap_inn_on_main_screen(mc['rest_town'])
self.inn_exist = {
	'valore': ["#FFFFFF", "0|1|#FFFFFF", [628, 203, 629, 205]],
	
self.inn_host_exist = {
	'valore': ["#A19E94", "13|-13|#9F9891, 4|5|#54544E", [696, 278, 710, 297]],


3.mc['wild_coord'] location from the new town

c.move_using_worldmap(mc['wild_coord'], wild_cat)
'hell-hornburg-pass': {
	'rest_town': 'berecain',
	'town_coord': [921, 307],
	'town_cat': 'world',
	'wild_coord': [359, 416],
	'wild_cat': 'hell',
	'init_mode': 1,
	'init_arr': [
		{
			'init_coord': [863, 444],
			'init_idle': 3,
		},
	],
