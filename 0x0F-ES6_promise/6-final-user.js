import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  let user;
  let pic;
  let statusUser;
  let statusPic;

  try {
    user = await signUpUser(firstName, lastName);
    statusUser = 'fulfilled';
  } catch (err) {
    user = err.toString();
    statusUser = 'rejected';
  }
  try {
    pic = await uploadPhoto(fileName);
    statusPic = 'fulfilled';
  } catch (err) {
    pic = err.toString();
    statusPic = 'rejected';
  }
  return [
    { value: user, status: statusUser },
    { value: pic, status: statusPic },
  ];
}
