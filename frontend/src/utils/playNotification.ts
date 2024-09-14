export const playNotification = (num: number = 1) => {
  // let url = "/delo_sdelano.mp3";
  // switch (num) {
  //   case 2:
  //     url = "/zdravstvuite_svetlana.mp3";
  //     break;
  //   case 3:
  //     url = "/ban4ik.m4a";
  //     break;
  //   case 4:
  //     url = "/eto_strashilka.mp3";
  //     break;
  //   default:
  //     break;
  // }
  const url = "/base_notification.mp3"
  const sound = new Audio(url);
  sound.volume = 0.1;
  sound.play();
};
