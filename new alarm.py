def alarm(seconds):
    time_elapsed = 0
    
    print(CLEAR) 
    
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        
        print(f"{CLEAR_AND_RETURN}EARS BLASTING IN! {minutes_left:02d}:{seconds_left:02d}")
    
    pygame.mixer.music.load(SOUND_FILE)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)


minutes = int(input("How many minutes? "))
seconds = int(input("How many seconds? "))

total_seconds = minutes * 60 + seconds
alarm(total_seconds)
