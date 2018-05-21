function get_link_through_ids(from_id, to_id) {
    var pk = document.getElementById(from_id).value;
    document.getElementById(to_id).setAttribute("href",pk);
}

function set_after(id) {
document.getElementById(id).setAttribute("src","/static/about_us/images/after.png")
}

function set_before(id) {
document.getElementById(id).setAttribute("src","/static/about_us/images/before.png")
}

function show_services(id, list, board){
    var j, items = [];

    if (board == "PRIEST")
        items.push("Pujari");

    if(board != 'PRIEST')
    for(var i=1; i<list.length;i=j) {
        i = list.indexOf(":", i);
        if(i == -1){
        break;
        }
        j = list.indexOf(">", i);
        items.push(list.slice(i+1, j));
    }
    var len = items.length;
    text = "";
    for (i = 0; i < len; i++) {
        text += "<li>" + items[i] + "</li>";
    }
    document.getElementById(id).innerHTML = text;
}

function play_music(to_id1, to_id2, music_url){
    var load_music = '<audio controls id="audio_player" autoplay style="width: 100%;">' +
        '<source id="' +to_id1 +'" src="'+music_url+'" type="audio/ogg">\n' +
        '<source id="' +to_id2 +'" src="'+music_url+'" type="audio/mpeg">\n' +
        'Your browser does not support the audio element.' +
        '</audio>';
    document.getElementById("audio_player").innerHTML = load_music;
    document.getElementById("audio_player").setAttribute("autoplay","");
}


function play_video(to_id1, to_id2, to_id3, video_url){
    var load_music = '<video controls id="video_player" autoplay style="width: 100%;">' +
        '<source id="' +to_id1 +'" src="'+video_url+'" type="video/mp4">\n' +
        '<source id="' +to_id2 +'" src="'+video_url+'" type="video/webm">\n' +
        '<source id="' +to_id3 +'" src="'+video_url+'" type="video/ogg">\n' +
        'Your browser does not support the video element.' +
        '</video>';
    document.getElementById("video_player").innerHTML = load_music;
    document.getElementById("video_player").setAttribute("autoplay","");
}


function validateMail(){
    var mail = document.getElementById("email").value;
    var pmail=/^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$/;
    if(mail.length == 0)
    	{
    	alert("Email Required");
    	return false;
    	}
    else if (!pmail.test(mail)) {
        alert("Email Format Incorrect");
        return false;
    }
    else if(pmail.test(mail)){
    	   return true;
     }
}

/*          NOT REQUIRED

function thanks_msg(id){
    alert("Hii");
    var textArray = [
    '.jif',
    '.png'
    ];
    var randomType = Math.floor(Math.random()*textArray.length);
    var randInt = getRandomIntInclusive(1, 5);
    document.getElementById(id).innerHTML = "<center><img src='/static/contact_us/images/thanks'.concat(randInt).concat(randomType)></center>";
    sleep(5);                      // calls method sleep defined below
}

function sleep(seconds){
    var waitUntil = new Date().getTime() + seconds*1000;
    while(new Date().getTime() < waitUntil) true;
}

function getRandomIntInclusive(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min; //The maximum is inclusive and the minimum is inclusive
}

*/
