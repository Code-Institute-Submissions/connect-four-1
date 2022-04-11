//Variables

const backgroundMusic = new Audio('../sounds/background-music.mp3')
const audioOnButton = document.getElementsByClassName("audio-on");
const audioOffButton = document.getElementsByClassName("audio-off");
let audioPlaying = false;

/**
 * Create an event listener for each of the audio icon buttons by looping through them.
 */
 audioOnButton.addEventListener('click', () => {
    toggleAudio();
});

audioOffButton.addEventListener('click', () => {
    toggleAudio();
});

/**
 * Let's the player choose to have sounds on or not
 * Loops through the audio buttons if sound is playing and adds the appropriate class in html
 * Loops through the audio buttons if soumd is not playing and adds the appropriate class in html
 */
function toggleAudio() {
    switch(audioPlaying){
        case false:
            toggleAudioOn();
            break;
        case true:
            toggleAudioOff();
            break;
    }
}

/**
 * If audioPlaying is true, update the audio button by looping through each of the buttons and adding the classlist accordingly
 * Play the background music immediately, set the volume and loop it through
 */
function toggleAudioOn() {
    audioPlaying = true;
    audioOnButton[i].classList.remove('hide');
    audioOffButton[i].classList.add('hide');
    backgroundMusic.volume = 0.1;
    backgroundMusic.play();
     //loop the background audio
    backgroundMusic.addEventListener('ended', function () {
        this.currentTime = 0;
        this.play();
    }, false);
}

/**
 * If audioPlaying is false, update the audio button accordingly
 * Looping through each of the audio buttons on the screens and adding the claslist accordingly
 * pause the background music
 */
function toggleAudioOff() {
    audioPlaying = false;
    audioOnButton[i].classList.add('hide');
    audioOffButton[i].classList.remove('hide');
    backgroundMusic.pause();
}