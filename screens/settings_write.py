def settings_write(reslist, volume_slider, help_yesno):
    with open("settings.txt", "w") as f:
        try:
            f.write("resolution"+","+reslist[c].split("x")[0]+","+reslist[c].split("x")[1])
            f.close()
        except:
            f.write("resolution,fullscreen")
            f.close()
    with open("settings.txt", "a") as f:
        f.write("\nvolume,"+str(volume_slider))
        f.close()
    with open("settings.txt", "a") as f:
        f.write("\nhelp,"+ help_yesno)
        f.close()




