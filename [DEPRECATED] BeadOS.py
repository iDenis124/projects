import time
import getpass
import webbrowser
import pyttsx3
import os
logo = r"""
 ____                    ____   _____
|  _ \                  / __ \ / ____|
| |_) | ___  __ _ _ __ | |  | | (___  
|  _ < / _ \/ _` | '_ \| |  | |\___ \ 
| |_) |  __/ (_| | | | | |__| |____) |
|____/ \___|\__,_|_| |_|\____/|_____/
"""
print(logo)
print("")
User = getpass.getuser()
engine = pyttsx3.init()
engine.say("Good day, {0}".format(User))
engine.runAndWait()
print("Opening the Bootloader")
a = 0


def clear(): return os.system('cls')


time.sleep(3)
print("Ensuring Dank Memes")
time.sleep(3)
print("Removing Past Data")
time.sleep(3)
print("Sprinkling some yiff...")
time.sleep(3)
print("DONE")
clear()
print("Hello, {0}!".format(User))


def MainMenu():
    print("Please choose an option")
    time.sleep(1)
    print("1: Dank Memes")
    print("2: The current time")
    print("3: Search google")
    print("4: 69")
    print("5: ok boomer")
    print("6: Funny gif")
    option = int(input("Please select a number\n"))
    if(option == 1):
        webbrowser.open("www.reddit.com/r/dankmemes")
        clear()
    elif(option == 2):
        t = time.localtime()
        print(time.strftime("%H:%M:%S", t))
        input("")
        clear()
    elif(option == 3):
        print("Did you kick your internet cable again?")
        input("")
        clear()
    elif(option == 4):
        print("nice")
        input("")
        clear()
    elif(option == 5):
        exit()
    elif(option == 6):
        webbrowser.open(r"https://media.discordapp.net/attachments/322051492548837376/610511067868823562/image0.gif?comment=Pigs_are_common_passive_mobs_that_spawn_in_the_Overworld._They_drop_porkchops_upon_death,_and_can_be_ridden_with_saddles._Pigs_typically_appear_in_the_Overworld_in_groups_of_4._They_randomly_oink._Pigs_move_similarly_to_other_passive_mobs;_they_wander_aimlessly,_and_avoid_lava_and_cliffs_high_enough_to_cause_fall_damage._They_make_no_attempt_to_stay_out_of_water,_bobbing_up_and_down_to_stay_afloat._When_they_encounter_obstacles,_pigs_often_hop_up_and_down,_apparently_attempting_to_jump_over_them_regardless_of_whether_it_is_possible._Pigs_can_be_pushed_into_minecarts_and_transported_by_rail._Pigs_follow_any_player_carrying_a_carrot,_carrot_on_a_stick,_potato,_or_beetroot,_and_stops_following_if_the_player_moves_farther_than_approximately_8_blocks_away_from_the_pig._When_a_pig_is_struck_by_lightning_or_hit_by_a_trident_with_the_Channeling_enchantment_during_a_thunderstorm,_it_transforms_into_a_zombie_pigman._If_the_pig_was_equipped_with_a_saddle,_the_saddle_is_lost,_and_a_mounted_player_is_ejected._Pigs_can_be_bred_using_carrots,_potatoes,_and_beetroots._It_takes_about_5_minutes_before_the_parents_can_be_bred_again,_as_with_all_farm_animals._It_takes_at_least_one_full_Minecraft_%27day%27_(20_minutes)_for_piglets_to_mature._The_appearance_of_a_piglet_is_roughly_similar_to_that_of_an_adult_pig,_having_the_same_sized_heads,_but_noticeably_smaller_bodies._Piglets_stay_near_their_parents_until_they_mature,_although_the_parents_cannot_protect_them_from_harm")
        engine.say("Pigs are common passive mobs that spawn in the Overworld. They drop porkchops upon death, and can be ridden with saddles. Pigs typically appear in the Overworld in groups of 4. They randomly oink. Pigs move similarly to other passive mobs; they wander aimlessly, and avoid lava and cliffs high enough to cause fall damage. They make no attempt to stay out of water, bobbing up and down to stay afloat. When they encounter obstacles, pigs often hop up and down, apparently attempting to jump over them regardless of whether it is possible. Pigs can be pushed into minecarts and transported by rail. Pigs follow any player carrying a carrot, carrot on a stick, potato, or beetroot, and stops following if the player moves farther than approximately 8 blocks away from the pig. When a pig is struck by lightning or hit by a trident with the Channeling enchantment during a thunderstorm, it transforms into a zombie pigman. If the pig was equipped with a saddle, the saddle is lost, and a mounted player is ejected. Pigs can be bred using carrots, potatoes, and beetroots. It takes about 5 minutes before the parents can be bred again, as with all farm animals. It takes at least one full Minecraft %27day%27 (20 minutes) for piglets to mature. The appearance of a piglet is roughly similar to that of an adult pig, having the same sized heads, but noticeably smaller bodies. Piglets stay near their parents until they mature, although the parents cannot protect them from harm")
        engine.runAndWait()
        clear()


while(1 == 1):
    MainMenu()
