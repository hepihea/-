

label debugMenu:
    menu:
       "{{DEBUG}}Set abuse 0...":
           $ abuse = 0
       "{{DEBUG}}Set abuse normal...":
           $ abuse = 2
       "{{DEBUG}}Set abuse to limit...":
           $ abuse = s_limit
    $ posCount = 0
    jump resetter
    jump prefuck

label resetter:
    #Position done once defs
    #Anal
    $ doneAnal = False
    $ doneRoughAnal = False
    $ doneAnalFast = False
    $ doneRoughAnalFast = False
    #Prone Anal
    $ doneProneAnal = False
    $ doneProneAnalFast = False
    $ doneProneAnalRough = False
    $ doneProneAnalRoughFast = False
    #Prone Vag
    $ doneProneVag = False
    $ doneProneVagFast = False
    $ doneProneVagRough = False
    $ doneProneVagRoughFast = False
    $ doneProneVagHappy = False
    $ doneProneVagHappyFast = False
    #Prone Vag
    $ doneProneVag = False
    $ doneProneVagFast = False
    $ doneProneVagRough = False
    $ doneProneVagRoughFast = False
    $ doneProneVagHappy = False
    $ doneProneVagHappyFast = False
    #Doggy
    $ doneDoggy = False
    $ doneDoggyFast = False
    $ doneRoughDoggy = False
    $ doneRoughDoggyFast = False
    $ doneHappyDoggy = False
    $ doneHappyDoggyFast = False
    #Missionary
    $ doneMissionary = False
    $ doneMissionaryFast = False
    $ doneRoughMissionary = False
    $ doneRoughMissionaryFast = False
    $ doneHappyMissionary = False
    $ doneHappyMissionaryFast = False
    #On Side
    $ doneSide = False
    $ doneRoughSide = False
    $ doneHappySide = False
    $ neverAnal = True
    jump prefuck
