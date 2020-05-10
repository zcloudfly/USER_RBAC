var categoryMap={
    '1':'招生信息',
    '2':'导师简介',
    '3':'学科简介',
    '4':'文件下载',
    '5':'学生论坛'
};
function getMapValue(map,key) {
        return map[key];
}
function getMapKey(map,v) {
    for(var key in map){
        if(v==map[key]){
            return key;
        }
    }
    return '';
}

