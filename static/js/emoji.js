//<link href="https://emoji-css.afeld.me/emoji.css" rel="stylesheet"/>

function convertemoji(text) {
    text = animals(text);
    text = text.replace(":tr", '<i class="em em-flag-tr"></i>');
    text = text.replace(":kalp", '<i class="em em-heart"></i>');
    text = text.replace(":galp", '<i class="em em-hearts"></i>');
    text = text.replace(":topla", '<i class="em em-heavy_plus_sign"></i>');
    text = text.replace(":sinirli", '<i class="em em-angry"></i>');
    return text;
}


function animals(text){
    text = text.replace(":kuş", '<i class="em em-bird"></i>');
    text = text.replace(":kedi", '<i class="em em-cat"></i>');
    text = text.replace(":karınca", '<i class="em em-ant"></i>');
    text = text.replace(":kokarca", '<i class="em em-badger"></i>');
    text = text.replace(":kedi2", '<i class="em em-cat2"></i>');
    text = text.replace(":leopar", '<i class="em em-leopard"></i>');
    text = text.replace(":aslan", '<i class="em em-lion_face"></i>');
    text = text.replace(":maymun", '<i class="em em-monkey_face"></i>');
    text = text.replace(":maymun2", '<i class="em em-monkey"></i>');
    text = text.replace(":fare", '<i class="em em-mouse"></i>');
    text = text.replace(":fare2", '<i class="em em-mouse_face"></i>');
    text = text.replace(":at", '<i class="em em-horse"></i>');
    text = text.replace(":yarışatı", '<i class="em em-horse_racing"></i>');
    text = text.replace(":balık", '<i class="em em-fish"></i>');
    text = text.replace(":ejderha", '<i class="em em-dragon"></i>');
    text = text.replace(":ejderha2", '<i class="em em-dragon_face"></i>');
    text = text.replace(":dog", '<i class="em em-dog"></i>');
    text = text.replace(":sincap", '<i class="em em-chipmunk"></i>');
    text = text.replace(":tavuk", '<i class="em em-chicken"></i>');
    text = text.replace(":civciv", '<i class="em em-baby_chick"></i>');
    text = text.replace(":civciv2", '<i class="em em-hatched_chick"></i>');
    text = text.replace(":civciv3", '<i class="em em-hatching_chick"></i>');
    text = text.replace(":yarasa", '<i class="em em-bat"></i>');
    text = text.replace(":ayı", '<i class="em em-bear"></i>');
    text = text.replace(":arı", '<i class="em em-bee"></i>');
    text = text.replace(":uğurböceği", '<i class="em em-beetle"></i>');
    text = text.replace(":balonbalığı", '<i class="em em-blowfish"></i>');
    text = text.replace(":yabandomuzu", '<i class="em em-boar"></i>');
    text = text.replace(":tırtıl", '<i class="em em-bug"></i>');
    text = text.replace(":kelebek", '<i class="em em-butterfly"></i>');
    text = text.replace(":deve", '<i class="em em-camel"></i>');
    text = text.replace(":deve", '<i class="em em-dromedary_camel"></i>');
    text = text.replace(":inek", '<i class="em em-cow"></i>');
    text = text.replace(":inek2", '<i class="em em-cow2"></i>');
    text = text.replace(":yengeç", '<i class="em em-crab"></i>');
    text = text.replace(":geyik", '<i class="em em-deer"></i>');
    text = text.replace(":köpek", '<i class="em em-dog"></i>');
    text = text.replace(":köpek2", '<i class="em em-dog2"></i>');
    text = text.replace(":yunusbalığı", '<i class="em em-dolphin"></i>');
    text = text.replace(":köpekbalığı", '<i class="em em-shark"></i>');
    text = text.replace(":kartal", '<i class="em em-eagle"></i>');
    text = text.replace(":fil", '<i class="em em-elephant"></i>');
    text = text.replace(":tilki", '<i class="em em-fox_face"></i>');
    text = text.replace(":kurbağa", '<i class="em em-frog"></i>');
    text = text.replace(":zürafa", '<i class="em em-giraffe_face"></i>');
    text = text.replace(":keçi", '<i class="em em-goat"></i>');
    text = text.replace(":keçi", '<i class="em em-goat"></i>');
    text = text.replace(":goril", '<i class="em em-gorilla"></i>');
    text = text.replace(":hamster", '<i class="em em-hamster"></i>');
    text = text.replace(":koala", '<i class="em em-koala"></i>');
    text = text.replace(":lama", '<i class="em em-llama"></i>');
    text = text.replace(":ıstakoz", '<i class="em em-lobster"></i>');
    text = text.replace(":baykuş", '<i class="em em-owl"></i>');
    text = text.replace(":ahtapot", '<i class="em em-octopus"></i>');
    text = text.replace(":boğa", '<i class="em em-ox"></i>');
    text = text.replace(":panda", '<i class="em em-panda_face"></i>');
    text = text.replace(":papağan", '<i class="em em-parrot"></i>');
    text = text.replace(":penguen", '<i class="em em-penguin"></i>');
    text = text.replace(":domuz", '<i class="em em-pig"></i>');
    text = text.replace(":domuz2", '<i class="em em-pig2"></i>');
    text = text.replace(":domuzburnu", '<i class="em em-pig_nose"></i>');
    text = text.replace(":tavşan", '<i class="em em-rabbit"></i>');
    text = text.replace(":tavşan2", '<i class="em em-rabbit2"></i>');
    text = text.replace(":rakun", '<i class="em em-raccoon"></i>');
    text = text.replace(":fare", '<i class="em em-rat"></i>');
    text = text.replace(":gergedan", '<i class="em em-rhinoceros"></i>');
    text = text.replace(":horoz", '<i class="em em-rooster"></i>');
    text = text.replace(":dinozor", '<i class="em em-sauropod"></i>');
    text = text.replace(":akrep", '<i class="em em-scorpion"></i>');
    text = text.replace(":dinozor", '<i class="em em-sauropod"></i>');
    text = text.replace(":koyun", '<i class="em em-sheep"></i>');
    text = text.replace(":karides", '<i class="em em-shrimp"></i>');
    text = text.replace(":yılan", '<i class="em em-snake"></i>');
    text = text.replace(":salyangoz", '<i class="em em-snail"></i>');
    text = text.replace(":kalamar", '<i class="em em-squid"></i>');
    text = text.replace(":kuğu", '<i class="em em-swan"></i>');
    text = text.replace(":örümcek", '<i class="em em-spider"></i>');
    text = text.replace(":hindi", '<i class="em em-turkey"></i>');
    text = text.replace(":trex", '<i class="em em-t-rex"></i>');
    text = text.replace(":kaplumbağa", '<i class="em em-turtle"></i>');
    text = text.replace(":kaplankafası", '<i class="em em-tiger"></i>');
    text = text.replace(":kaplan", '<i class="em em-tiger2"></i>');
    text = text.replace(":tropikbalık", '<i class="em em-tropical_fish"></i>');
    text = text.replace(":asyamandası", '<i class="em em-water_buffalo"></i>');
    text = text.replace(":balina", '<i class="em em-whale"></i>');
    text = text.replace(":balina2", '<i class="em em-whale2"></i>');
    text = text.replace(":kurt", '<i class="em em-wolf"></i>');
    text = text.replace(":zebra", '<i class="em em-zebra_face"></i>');
    return text;
}
