export const playNotification = () => {
  const sound = new Audio("/wet-431.mp3");
  sound.volume = 0.4;
  sound.play();
};
