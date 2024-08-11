export const playNotification = (num: number = 1) => {
  let url = "/delo_sdelano.mp3";
  switch (num) {
    case 2:
      url = "/zdravstvuite_svetlana.mp3";
      break;
    default:
      break;
  }
  const sound = new Audio(url);
  sound.volume = 1;
  sound.play();
};
