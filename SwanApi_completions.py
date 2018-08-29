import sublime, sublime_plugin

swanApi = [
# ("swan", "swan"),

("swan.request\tapi", "swan.request($0);"),
("swan.request\tsnippet", "swan.request({${2:\n}    ${4:url: '$1'}${3:\n}});"),
("swan.uploadFile\tapi", "swan.uploadFile($0);"),
("swan.uploadFile\tsnippet", "swan.uploadFile({${2:\n}    ${8:url: '$1',}${3:\n}    ${4:filePath: '',}${5:\n}    ${6:name: ''}${7:\n}});"),
("swan.downloadFile\tapi", "swan.downloadFile($0);"),
("swan.downloadFile\tsnippet", "swan.downloadFile({${2:\n}    ${4:url: '$1'}${3:\n}});"),
("swan.connectSocket\tapi", "swan.connectSocket($0);"),
("swan.connectSocket\tsnippet", "swan.connectSocket({${2:\n}    ${4:url: '$1'}${3:\n}});"),
("swan.onSocketOpen\tapi", "swan.onSocketOpen($0);"),
("swan.onSocketOpen\tsnippet", "swan.onSocketOpen(function(res) {${2:\n}    $1${3:\n}});"),
("swan.onSocketError\tapi", "swan.onSocketError($0);"),
("swan.onSocketError\tsnippet", "swan.onSocketError(function(res) {${2:\n}    $1${3:\n}});"),
("swan.sendSocketMessage\tapi", "swan.sendSocketMessage($0);"),
("swan.sendSocketMessage\tsnippet", "swan.sendSocketMessage({${2:\n}    ${4:data: '$1'}${3:\n}});"),
("swan.onSocketMessage\tapi", "swan.onSocketMessage($0);"),
("swan.onSocketMessage\tsnippet", "swan.onSocketMessage(function(res) {${2:\n}    $1${3:\n}};"),
("swan.closeSocket\tapi", "swan.closeSocket();$0"),
("swan.onSocketClose\tapi", "swan.onSocketClose($0);"),
("swan.onSocketClose\tsnippet", "swan.onSocketClose(function(res) {${2:\n}    $1${3:\n}});"),
("SocketTask.send\tapi", "SocketTask.send($0);"),
("SocketTask.send\tsnippet", "SocketTask.send({${2:\n}    ${4:data: '$1'}${3:\n}});"),
("SocketTask.close\tapi", "SocketTask.close($0);"),
("SocketTask.onOpen\tapi", "SocketTask.onOpen($0);"),

("swan.ai", "swan.ai"),
("swan.ai.ocrIdCard\tapi", "swan.ai.ocrIdCard($0);"),
("swan.ai.ocrIdCard\tsnippet", "swan.ai.ocrIdCard({${2:\n}    ${4:image: '$1'}${3:\n}});"),
("swan.ai.ocrBankCard\tapi", "swan.ai.ocrBankCard($0);"),
("swan.ai.ocrBankCard\tsnippet", "swan.ai.ocrBankCard({${2:\n}    ${4:image: '$1'}${3:\n}});"),
("swan.ai.ocrDrivingLicense\tapi", "swan.ai.ocrDrivingLicense($0);"),
("swan.ai.ocrDrivingLicense\tsnippet", "swan.ai.ocrDrivingLicense({${2:\n}    ${4:image: '$1'}${3:\n}});"),
("swan.ai.ocrVehicleLicense\tapi", "swan.ai.ocrVehicleLicense($0);"),
("swan.ai.ocrVehicleLicense\tsnippet", "swan.ai.ocrVehicleLicense({${2:\n}    ${4:image: '$1'}${3:\n}});"),
("swan.ai.textReview\tapi", "swan.ai.textReview($0);"),
("swan.ai.textReview\tsnippet", "swan.ai.textReview({${2:\n}    ${4:content: '$1'}${3:\n}});"),
("swan.ai.textToAudio\tapi", "swan.ai.textToAudio($0);"),
("swan.ai.textToAudio\tsnippet", "swan.ai.textToAudio({${2:\n}    ${8:tex: '$1',}${3:\n}    ${4:ctp: '',}${5:\n}    ${6:lan: ''}${7:\n}});"),
("swan.ai.imageAudit\tapi", "swan.ai.imageAudit($0);"),
("swan.ai.imageAudit\tsnippet", "swan.ai.imageAudit({${2:\n}    ${4:image: '$1'}${3:\n}});"),
("swan.ai.advancedGeneralIdentify\tapi", "swan.ai.advancedGeneralIdentify($0);"),
("swan.ai.advancedGeneralIdentify\tsnippet", "swan.ai.advancedGeneralIdentify({${2:\n}    ${4:image: '$1'}${3:\n}});"),
("swan.ai.objectDetectIdentify\tapi", "swan.ai.objectDetectIdentify($0);"),
("swan.ai.objectDetectIdentify\tsnippet", "swan.ai.objectDetectIdentify({${2:\n}    ${4:image: '$1'}${3:\n}});"),
("swan.ai.carClassify\tapi", "swan.ai.carClassify($0);"),
("swan.ai.carClassify\tsnippet", "swan.ai.carClassify({${2:\n}    ${4:image: '$1'}${3:\n}});"),
("swan.ai.dishClassify\tapi", "swan.ai.dishClassify($0);"),
("swan.ai.dishClassify\tsnippet", "swan.ai.dishClassify({${2:\n}    ${4:image: '$1'}${3:\n}});"),
("swan.ai.logoClassify\tapi", "swan.ai.logoClassify($0);"),
("swan.ai.logoClassify\tsnippet", "swan.ai.logoClassify({${2:\n}    ${4:image: '$1'}${3:\n}});"),
("swan.ai.animalClassify\tapi", "swan.ai.animalClassify($0);"),
("swan.ai.animalClassify\tsnippet", "swan.ai.animalClassify({${2:\n}    ${4:image: '$1'}${3:\n}});"),
("swan.ai.plantClassify\tapi", "swan.ai.plantClassify($0);"),
("swan.ai.plantClassify\tsnippet", "swan.ai.plantClassify({${2:\n}    ${4:image: '$1'}${3:\n}});"),

("swan.chooseImage\tapi", "swan.chooseImage($0);"),
("swan.chooseImage\tsnippet", "swan.chooseImage({${2:\n}    success: function (res) {$1}${3:\n}});"),
("swan.previewImage\tapi", "swan.previewImage($0);"),
("swan.previewImage\tsnippet", "swan.previewImage({${2:\n}    ${4:urls: '$1'}${3:\n}});"),
("swan.getImageInfo\tapi", "swan.getImageInfo($0);"),
("swan.getImageInfo\tsnippet", "swan.getImageInfo({${2:\n}    ${4:src: '$1'}${3:\n}});"),
("swan.saveImageToPhotosAlbum\tapi", "swan.saveImageToPhotosAlbum($0);"),
("swan.saveImageToPhotosAlbum\tsnippet", "swan.saveImageToPhotosAlbum({${2:\n}    ${4:filePath: '$1'}${3:\n}});"),
# 录音管理 待补充
("swan.getRecorderManager\tapi", "swan.getRecorderManager();$0"),

# 背景音频 待补充
("swan.getBackgroundAudioManager\tapi", "swan.getBackgroundAudioManager();$0"),

# 音频组建控制 待补充
("swan.createInnerAudioContext\tapi", "swan.createInnerAudioContext();$0"),

("swan.chooseVideo\tapi", "swan.chooseVideo($0);"),
("swan.chooseVideo\tsnippet", "swan.chooseVideo({${2:\n}    success: function (res) {$1}${3:\n}});"),
("swan.saveVideoToPhotosAlbum\tapi", "swan.saveVideoToPhotosAlbum($0);"),
("swan.saveVideoToPhotosAlbum\tsnippet", "swan.saveVideoToPhotosAlbum({${2:\n}    ${4:filePath: '$1'}${3:\n}});"),

("swan.createVideoContext\tapi", "swan.createVideoContext('$0');"),
("pause\tfunction", "pause();$0"),
("seek\tfunction", "seek(${1:positon});"),
("sendDanmu\tfunction", "sendDanmu(${1:danmu});"),
("requestFullScreen\tfunction", "requestFullScreen();$0"),

("swan.createLivePlayerContext\tapi", "swan.createLivePlayerContext('$0');"),
("play\tfunction", "play();$0"),
("stop\tfunction", "stop($0);"),
("mute\tfunction", "mute($0);"),
("requestFullScreen\tsnippet", "requestFullScreen({${2:\n}    ${4:direction: $1}${3:\n}});"),
("exitFullScreen\tfunction", "exitFullScreen();$0"),

("swan.createCameraContext\tapi", "swan.createCameraContext();$0"),
("takePhoto\tfunction", "takePhoto({${2:\n}    $1${3:\n}});"),
("startRecord\tfunction", "startRecord({${2:\n}    $1${3:\n}});"),
("stopRecord\tfunction", "stopRecord({${2:\n}    $1${3:\n}});"),

("swan.saveFile\tapi", "swan.saveFile($0);"),
("swan.saveFile\tsnippet", "swan.saveFile({${2:\n}    ${4:tempFilePath: '$1'}${3:\n}});"),
("swan.getFileInfo\tapi", "swan.getFileInfo($0);"),
("swan.getFileInfo\tsnippet", "swan.getFileInfo({${2:\n}    ${4:filePath: '$1'}${3:\n}});"),
("swan.getSavedFileList\tapi", "swan.getSavedFileList($0);"),
("swan.getSavedFileList\tsnippet", "swan.getSavedFileList({${2:\n}    $1${3:\n}});"),
("swan.getSavedFileInfo\tapi", "swan.getSavedFileInfo($0);"),
("swan.getSavedFileInfo\tsnippet", "swan.getSavedFileInfo({${2:\n}    ${4:filePath: '$1'}${3:\n}});"),

("swan.removeSavedFile\tapi", "swan.removeSavedFile($0);"),
("swan.removeSavedFile\tsnippet", "swan.removeSavedFile({${2:\n}    ${4:filePath: '$1'}${3:\n}});"),

("swan.openDocument\tapi", "swan.openDocument($0);"),
("swan.openDocument\tsnippet", "swan.openDocument({${2:\n}    ${4:filePath: '$1'}${3:\n}});"),

("swan.setStorage\tapi", "swan.setStorage($0);"),
("swan.setStorage\tsnippet", "swan.setStorage({${2:\n}    ${6:key: '$1',}${3:\n}    ${4:data: ''}${5:\n}});"),
("swan.setStorageSync\tapi", "swan.setStorageSync(${1:key}, ${2:value});"),
("swan.getStorage\tapi", "swan.getStorage($0);"),
("swan.getStorage\tsnippet", "swan.getStorage({${2:\n}    ${6:key: '$1',}${3:\n}    success: function (res) {$4}${5:\n}});"),
("swan.getStorageSync\tapi", "swan.getStorageSync('$0');"),
("swan.getStorageInfo\tapi", "swan.getStorageInfo($0);"),
("swan.getStorageInfo\tsnippet", "swan.getStorageInfo({${2:\n}    success: function (res) {$1}${3:\n}});"),
("swan.getStorageInfoSync\tapi", "swan.getStorageInfoSync();$0"),

("swan.removeStorage\tapi", "swan.removeStorage($0);"),
("swan.removeStorage\tsnippet", "swan.removeStorage({${2:\n}    ${6:key: '$1',}${3:\n}    success: function (res) {$4}${5:\n}});"),
("swan.removeStorageSync\tapi", "swan.removeStorageSync('$0');"),
("swan.clearStorage\tapi", "swan.clearStorage($0);"),
("swan.clearStorage\tsnippet", "swan.clearStorage({${2:\n}    success: function (res) {$1}${3:\n}});"),
("swan.clearStorageSyn\tapi", "swan.clearStorageSyn();$0"),

("swan.getLocation\tapi", "swan.getLocation($0);"),
("swan.getLocation\tsnippet", "swan.getLocation({${2:\n}    success: function (res) {$1}${3:\n}});"),
("swan.chooseLocation\tapi", "swan.chooseLocation($0);"),
("swan.chooseLocation\tsnippet", "swan.chooseLocation({${2:\n}    $1${3:\n}});"),

("swan.openLocation\tapi", "swan.openLocation($0);"),
("swan.openLocation\tsnippet", "swan.openLocation({${2:\n}    ${4:latitude: $1,}${3:\n}    ${5:longitude: $6}${7:\n}});"),

("swan.createMapContext\tapi", "swan.createMapContext('$0');"),
("getCenterLocation\tfunction", "getCenterLocation({${2:\n}    $1${3:\n}});"),
("moveToLocation\tfunction", "moveToLocation();$0"),
("translateMarker\tfunction", "translateMarker({${2:\n}    ${4:markerId: $1,}${3:\n}    ${5:destination: $6,}${7:\n}    ${8:autoRotate: $9,}${10:\n}    ${11:rotate: $12,}${13:\n}});"),
("includePoints\tfunction", "includePoints({${2:\n}    ${4:points: $1}${3:\n}});"),
("getRegion\tfunction", "getRegion({${2:\n}    $1${3:\n}});"),
("getScale\tfunction", "getScale({${2:\n}    $1${3:\n}});"),


("this.createCanvasContext\tapi", "this.createCanvasContext('$0');"),
("swan.createCanvasContext\tapi", "swan.createCanvasContext('$0');"),
("swan.canvasToTempFilePath\tapi", "swan.canvasToTempFilePath($0);"),
("swan.canvasToTempFilePath\tsnippet", "swan.canvasToTempFilePath({${2:\n}    ${4:canvasId: '$1'}${3:\n}});"),
("setFillStyle\tapi", "setFillStyle('$0');"),
("setStrokeStyle\tapi", "setStrokeStyle('$0');"),
("setShadow\tapi", "setShadow(${1:offsetX}, ${2:offsetY}, ${3:blur}, ${4:color});"),
("createLinearGradient\tapi", "createLinearGradient(${1:x0}, ${2:y0}, ${3:x1}, ${4:y1});"),
("createCircularGradient\tapi", "createCircularGradient(${1:x}, ${2:y}, ${3:r});"),
("addColorStop\tapi", "addColorStop(${1:stop}, ${2:color});"),
("setLineWidth\tapi", "setLineWidth(${1:lineWidth});"),
("setLineCap\tapi", "setLineCap('${1:butt}');"),
("setLineJoin\tapi", "setLineJoin('${1:bevel}');"),
("setLineDash\tapi", "setLineDash(${1:pattern}, ${2:offset});"),
("setMiterLimit\tapi", "setMiterLimit(${1:miterLimit});"),
("rect\tapi", "rect(${1:x}, ${2:y}, ${3:width}, ${4:height});"),
("fillRect\tapi", "fillRect(${1:x}, ${2:y}, ${3:width}, ${4:height});"),
("strokeRect\tapi", "strokeRect(${1:x}, ${2:y}, ${3:width}, ${4:height});"),
("clearRect\tapi", "clearRect(${1:x}, ${2:y}, ${3:width}, ${4:height});"),
("fill\tapi", "fill();$0"),
("stroke\tapi", "stroke();$0"),
("beginPath\tapi", "beginPath();$0"),
("closePath\tapi", "closePath();$0"),
("moveTo\tapi", "moveTo(${1:x}, ${2:y});"),
("lineTo\tapi", "lineTo(${1:x}, ${2:y});"),
("arc\tapi", "arc(${1:x}, ${2:y}, ${3:r});"),
("scale\tapi", "scale(${1:scaleWidth}, ${2:scaleHeight});"),
("rotate\tapi", "rotate(${1:rotate});"),
("translate\tapi", "translate(${1:x}, ${2:y});"),
("clip\tapi", "clip();$0"),
("setFontSize\tapi", "setFontSize(${1:fontSize});"),
("fillText\tapi", "fillText(${1:text}, ${2:x}, ${3:y});"),
("setTextAlign\tapi", "setTextAlign('${1:left}');"),
("setTextBaseline\tapi", "setTextBaseline('${1:top}');"),
("drawImage\tapi", "drawImage(${1:src}, ${2:dx}, ${3:dy}, ${4:dWidth}, ${5:dHeight});"),
("setGlobalAlpha\tapi", "setGlobalAlpha(${1:alpha});"),
("measureText\tapi", "measureText(${1:text});"),
("arcTo\tapi", "arcTo(${1:x0}, ${2:y0}, ${3:x1}, ${4:y1}), ${5:r};"),
("strokeText\tapi", "strokeText(${1:text}, ${2:x}, ${3:y}, ${4:maxWidth});"),
("setLineDashOffset\tapi", "setLineDashOffset =${1:value};"),
("createPattern\tapi", "createPattern(${1:src}, '${2:repeat-x}');"),
("bezierCurveTo\tapi", "bezierCurveTo(${1:cp1x}, ${2:cp1y}, ${3:cp2x}, ${4:cp2y}, ${5:x}, ${6:y});"),
("quadraticCurveTo\tapi", "quadraticCurveTo(${1:cpx}, ${2:cpy}, ${3:x}, ${4:y});"),
("save\tapi", "save();$0"),
("restore\tapi", "restore();$0"),
("draw\tapi", "draw();$0"),
("font\tapi", "font =${1:value};"),
("setTransform\tapi", "setTransform(${1:scaleX}, ${2:skewX}, ${3:skewY}, ${4:scaleY}, ${5:translateX}, ${6:translateY});"),


("swan.showToast\tapi", "swan.showToast($0);"),
("swan.showToast\tsnippet", "swan.showToast({${2:\n}    ${4:title: '$1'}${3:\n}});"),
("swan.showLoading\tapi", "swan.showLoading($0);"),
("swan.showLoading\tsnippet", "swan.showLoading({${2:\n}    ${4:title: '$1'}${3:\n}});"),
("swan.hideToast\tapi", "swan.hideToast();$0"),
("swan.showModal\tapi", "swan.showModal($0);"),
("swan.showModal\tsnippet", "swan.showModal({${2:\n}    ${6:title: '$1',}${3:\n}    ${4:content: ''}${5:\n});"),
("swan.showActionSheet\tapi", "swan.showActionSheet($0);"),
("swan.showActionSheet\tsnippet", "swan.showActionSheet({${2:\n}    ${4:itemList: [$1]}${3:\n}});"),

("swan.setNavigationBarTitle\tapi", "swan.setNavigationBarTitle($0);"),
("swan.setNavigationBarTitle\tsnippet", "swan.setNavigationBarTitle({${2:\n}    ${4:title: '$1'}${3:\n}});"),
("swan.showNavigationBarLoading\tapi", "swan.showNavigationBarLoading();$0"),
("swan.hideNavigationBarLoading\tapi", "swan.hideNavigationBarLoading();$0"),
("swan.setNavigationBarColor\tapi", "swan.setNavigationBarColor($0);"),
("swan.setNavigationBarColor\tsnippet", "swan.setNavigationBarColor({${2:\n}    ${6:frontColor: '$1',}${3:\n}    ${4:backgroundColor: ''}${5:\n}});"),
("swan.setTabBarBadge\tapi", "swan.setTabBarBadge($0);"),
("swan.setTabBarBadge\tsnippet", "swan.setTabBarBadge({${2:\n}    ${6:index: $1,}${3:\n}    ${4:text: ''}${5:\n}});"),
("swan.removeTabBarBadge\tapi", "swan.removeTabBarBadge($0);"),
("swan.removeTabBarBadge\tsnippet", "swan.removeTabBarBadge({${2:\n}    ${4:index: $1}${3:\n}});"),
("swan.showTabBarRedDot\tapi", "swan.showTabBarRedDot($0);"),
("swan.showTabBarRedDot\tsnippet", "swan.showTabBarRedDot({${2:\n}    ${4:index: $1}${3:\n}});"),
("swan.hideTabBarRedDot\tapi", "swan.hideTabBarRedDot($0);"),
("swan.hideTabBarRedDot\tsnippet", "swan.hideTabBarRedDot({${2:\n}    ${4:index: $1}${3:\n}});"),
("swan.setTabBarStyle\tapi", "swan.setTabBarStyle($0);"),
("swan.setTabBarStyle\tsnippet", "swan.setTabBarStyle({${2:\n}    ${10:color: '$1',}${3:\n}    ${4:selectedColor: '',}${5:\n}    ${6:backgroundColor: '',}${7:\n}    ${8:borderStyle: '',}${9:\n}});"),
("swan.setTabBarItem\tapi", "swan.setTabBarItem($0);"),
("swan.setTabBarItem\tsnippet", "swan.setTabBarItem({${2:\n}    ${8:index: $1,}${3:\n}    ${4:text: '',}${5:\n}    ${6:iconPath: '',}${7:\n}    ${8:selectedIconPath: '',}${9:\n}});"),
("swan.showTabBar\tapi", "swan.showTabBar($0);"),
("swan.showTabBar\tsnippet", "swan.showTabBar({${2:\n}    $1${3:\n}});"),
("swan.hideTabBar\tapi", "swan.hideTabBar($0);"),
("swan.hideTabBar\tsnippet", "swan.hideTabBar({${2:\n}    $1${3:\n}});"),

("swan.navigateTo\tapi", "swan.navigateTo($0);"),
("swan.navigateTo\tsnippet", "swan.navigateTo({${2:\n}    ${4:url: '$1'}${3:\n}});"),
("swan.redirectTo\tapi", "swan.redirectTo($0);"),
("swan.redirectTo\tsnippet", "swan.redirectTo({${2:\n}    ${4:url: '$1'}${3:\n}});"),
("swan.switchTab\tapi", "swan.switchTab($0);"),
("swan.switchTab\tsnippet", "swan.switchTab({${2:\n}    ${4:url: '$1'}${3:\n}});"),
("swan.navigateBack\tapi", "swan.navigateBack($0);"),
("swan.navigateBack\tsnippet", "swan.navigateBack({${2:\n}    $1${3:\n}});"),
("swan.reLaunch\tapi", "swan.reLaunch($0);"),
("swan.reLaunch\tsnippet", "swan.reLaunch({${2:\n}    ${4:url: '$1'}${3:\n}});"),

("swan.createAnimation\tapi", "swan.createAnimation($0);"),
("swan.createAnimation\tsnippet", "swan.createAnimation({${2:\n}    $1${3:\n}});"),

("swan.pageScrollTo\tapi", "swan.pageScrollTo($0);"),
("swan.pageScrollTo\tsnippet", "swan.pageScrollTo({${2:\n}    ${4:scrollTop: $1}${3:\n}});"),

("onPullDownRefresh\tfunction", "onPullDownRefresh() {${2:\n}    $1${3:\n}};"),
("swan.startPullDownRefresh\tapi", "swan.startPullDownRefresh();$0"),
("swan.startPullDownRefresh\tsnippet", "swan.startPullDownRefresh({${2:\n}    $1${3:\n}});"),
("swan.stopPullDownRefresh\tapi", "swan.stopPullDownRefresh();$0"),


("swan.createSelectorQuery\tfunction", "swan.createSelectorQuery();$0"),
("in\tapi", "in(${1:this});"),
("select\tapi", "select($0);"),
("selectAll\tapi", "selectAll($0);"),
("selectViewport\tapi", "selectViewport();$0"),
("boundingClientRect\tapi", "boundingClientRect(rects) {${2:\n}    $1${3:\n}};"),
("scrollOffset\tapi", "scrollOffset(res) {${2:\n}    $1${3:\n}};"),
("fields\tapi", "fields({${2:\n}    $1${3:\n}});"),
("exec\tapi", "exec();$0"),

("swan.getSystemInfo\tapi", "swan.getSystemInfo($0);"),
("swan.getSystemInfo\tsnippet", "swan.getSystemInfo({${2:\n}    success: function (res) {$1}${3:\n}});"),
("swan.getSystemInfoSync\tapi", "swan.getSystemInfoSync();$0"),
("swan.canIUse\tapi", "swan.canIUse('$0');"),

("swan.onMemoryWarning\tsnippet", "swan.onMemoryWarning(function (res) {${2:\n}    $1${3:\n}});"),

("swan.getNetworkType\tapi", "swan.getNetworkType($0);"),
("swan.getNetworkType\tsnippet", "swan.getNetworkType({${2:\n}    success: function (res) {$1}${3:\n}});"),
("swan.onNetworkStatusChange\tapi", "swan.onNetworkStatusChange($0);"),
("swan.onNetworkStatusChange\tsnippet", "swan.onNetworkStatusChange({${2:\n}    success: function (res) {$1}${3:\n}});"),

("swan.onAccelerometerChange\tapi", "swan.onAccelerometerChange($0);"),
("swan.onAccelerometerChange\tsnippet", "swan.onAccelerometerChange({${2:\n}    success: function (res) {$1}${3:\n}});"),
("swan.startAccelerometer\tapi", "swan.startAccelerometer($0);"),
("swan.startAccelerometer\tsnippet", "swan.startAccelerometer({${2:\n}    $1${3:\n}});"),
("swan.stopAccelerometer\tapi", "swan.stopAccelerometer($0);"),
("swan.stopAccelerometer\tsnippet", "swan.stopAccelerometer({${2:\n}    $1${3:\n}});"),

("swan.onCompassChange\tapi", "swan.onCompassChange($0);"),
("swan.onCompassChange\tsnippet", "swan.onCompassChange({${2:\n}    success: function (res) {$1}${3:\n}});"),
("swan.startCompass\tapi", "swan.startCompass($0);"),
("swan.startCompass\tsnippet", "swan.startCompass({${2:\n}    $1${3:\n}});"),
("swan.stopCompass\tapi", "swan.stopCompass($0);"),
("swan.stopCompass\tsnippet", "swan.stopCompass({${2:\n}    $1${3:\n}});"),

("swan.scanCode\tapi", "swan.scanCode($0);"),
("swan.scanCode\tsnippet", "swan.scanCode({${2:\n}    $1${3:\n}});"),

("swan.setScreenBrightness\tapi", "swan.setScreenBrightness($0);"),
("swan.setScreenBrightness\tsnippet", "swan.setScreenBrightness({${2:\n}    ${4:value: $1}${3:\n}});"),
("swan.getScreenBrightness\tapi", "swan.getScreenBrightness($0);"),
("swan.getScreenBrightness\tsnippet", "swan.getScreenBrightness({${2:\n}    success: function (res) {$1}${3:\n}});"),
("swan.setKeepScreenOn\tapi", "swan.setKeepScreenOn($0);"),
("swan.setKeepScreenOn\tsnippet", "swan.setKeepScreenOn({${2:\n}    keepScreenOn: ${1:true}${3:\n}});"),

("swan.onUserCaptureScreen\tsnippet", "swan.onUserCaptureScreen(function () {${2:\n}    $1${3:\n}});"),

("swan.vibrateLong\tapi", "swan.vibrateLong($0);"),
("swan.vibrateLong\tsnippet", "swan.vibrateLong({${2:\n}    $1${3:\n}});"),
("swan.vibrateShort\tapi", "swan.vibrateShort($0);"),
("swan.vibrateShort\tsnippet", "swan.vibrateShort({${2:\n}    $1${3:\n}});"),

("swan.addPhoneContact\tapi", "swan.addPhoneContact($0);"),
("swan.addPhoneContact\tsnippet", "swan.addPhoneContact({${2:\n}    ${4:firstName: '$1'}${3:\n}});"),

("swan.makePhoneCall\tapi", "swan.makePhoneCall($0);"),
("swan.makePhoneCall\tsnippet", "swan.makePhoneCall({${2:\n}    ${4:phoneNumber: '$1'}${3:\n}});"),

("swan.setClipboardData\tapi", "swan.setClipboardData($0);"),
("swan.setClipboardData\tsnippet", "swan.setClipboardData({${2:\n}    ${4:data: '$1'}${3:\n}});"),
("swan.getClipboardData\tapi", "swan.getClipboardData($0);"),
("swan.getClipboardData\tsnippet", "swan.getClipboardData({${2:\n}    success: function (res) {$1}${3:\n}});"),

("swan.getExtConfig\tapi", "swan.getExtConfig($0);"),
("swan.getExtConfig\tsnippet", "swan.getExtConfig({${2:\n}    success: function (res) {$1}${3:\n}});"),
("swan.getExtConfigSync\tapi", "swan.getExtConfigSync();$0"),

("swan.login\tapi", "swan.login($0);"),
("swan.login\tsnippet", "swan.login({${2:\n}    success: function (res) {$1}${3:\n}});"),
("swan.checkSession\tapi", "swan.checkSession($0);"),
("swan.checkSession\tsnippet", "swan.checkSession({${2:\n}    success: function (res) {$1}${3:\n}});"),
("swan.authorize\tapi", "swan.authorize($0);"),
("swan.authorize\tsnippet", "swan.authorize({${2:\n}    scope: '$1'${3:\n}    success: function (res) {$4}${5:\n}});"),
("swan.getSwanId\tapi", "swan.getSwanId($0);"),
("swan.getSwanId\tsnippet", "swan.getSwanId({${2:\n}    success: function (res) {$1}${3:\n}});"),
("swan.getUserInfo\tapi", "swan.getUserInfo($0);"),
("swan.getUserInfo\tsnippet", "swan.getUserInfo({${2:\n}    success: function (res) {$1}${3:\n}});"),
("swan.openSetting\tapi", "swan.openSetting($0);"),
("swan.openSetting\tsnippet", "swan.openSetting({${2:\n}    success: function (res) {$1}${3:\n}});"),
("swan.getSetting\tapi", "swan.getSetting($0);"),
("swan.getSetting\tsnippet", "swan.getSetting({${2:\n}    success: function (res) {$1}${3:\n}});"),
("onShareAppMessage\tapi", "onShareAppMessage($0);"),
("onShareAppMessage\tsnippet", "onShareAppMessage() {${2:\n}    return {${3:\n}        title: '$1',${4:\n}        content: '',${5:\n}        path: ''${6:\n}    };${7:\n}}"),
("swan.chooseAddress\tapi", "swan.chooseAddress($0);"),
("swan.chooseAddress\tsnippet", "swan.chooseAddress({${2:\n}    success: function (res) {$1}${3:\n}});"),
("swan.requestPolymerPayment \tapi", "swan.requestPolymerPayment ($0);"),
("swan.requestPolymerPayment \tsnippet", "swan.requestPolymerPayment ({${2:\n}    orderInfo: {$1},${3:\n}    success: function (res) {$4}${5:\n}});"),
("swan.chooseInvoiceTitle\tapi", "swan.chooseInvoiceTitle($0);"),
("swan.chooseInvoiceTitle\tsnippet", "swan.chooseInvoiceTitle({${2:\n}    success: function (res) {$1}${3:\n}});"),
("swan.navigateToSmartProgram\tapi", "swan.navigateToSmartProgram($0);"),
("swan.navigateToSmartProgram\tsnippet", "swan.navigateToSmartProgram({${2:\n}    appKey: '$1'${3:\n}});"),
("swan.navigateBackSmartProgram\tapi", "swan.navigateBackSmartProgram($0);"),
("swan.navigateBackSmartProgram\tsnippet", "swan.navigateBackSmartProgram({${2:\n}    success: function (res) {$1}${3:\n}});"),

("success\tcallback", "success: function (res) {${2:\n}    $1${3:\n}}"),
("fail\tcallback", "fail: function (res) {${2:\n}    $1${3:\n}}"),
("complete\tcallback", "complete: function (res) {${2:\n}    $1${3:\n}}"),
]

# could use different lists

completions = list(swanApi)

# These are characters that select the first item in an open autocomplete window when pressed.
fillup_chars = "~`!#%^&*()-=+{}[]|\\;:'\",.<>?/"
# These are characters that close the autocomplete window when pressed.
stop_chars = "~`!@#%^&*()-=+{}[]|\\;:'\",<>?/ "

def hide_auto_complete(view):
        view.run_command('hide_auto_complete')

def show_auto_complete(view,
                       disable_auto_insert=True, api_completions_only=True,
                       next_completion_if_showing=True, auto_complete_commit_on_tab=True):
    # Show autocompletions:
    def _show_auto_complete():
        view.run_command('auto_complete', {
            'disable_auto_insert': disable_auto_insert,
            'api_completions_only': api_completions_only,
            'next_completion_if_showing': next_completion_if_showing,
            'auto_complete_commit_on_tab': auto_complete_commit_on_tab,
        })
    sublime.set_timeout(_show_auto_complete, 0)

class SwanApiCompletions(sublime_plugin.EventListener):

    def on_query_completions(self, view, prefix, locations):
        global compAll
        if not (view.match_selector(locations[0],
                                    'source.js -string -comment -constant') or
                view.match_selector(locations[0],
                                    'source.ts -string -comment -constant')):
            return []
        # pt = locations[0] - len(prefix) - 1
        # # get the character before the trigger
        # ch = view.substr(sublime.Region(pt, pt + 1)) if pt >= 0 else None
        # word = view.word(pt - 1) if pt >= 0 else None
        # word = view.substr(word) if word is not None else None
        # if word is None:
        #     hide_auto_complete(view)

        view_sel = view.sel()
        if not view_sel:
            return

        sel = view_sel[0]
        pos = sel.end()
        next_char = view.substr(sublime.Region(pos - 1, pos))

        if next_char == '\n':
            return

        is_fill_char = next_char and next_char in fillup_chars
        is_stop_char = next_char and next_char in stop_chars
        
        # Stop characters hide autocomplete window
        if is_stop_char:
            hide_auto_complete(view)

        compDefault = [view.extract_completions(prefix)]
        compDefault = [(item + "\tDefault", item) for sublist in compDefault 
            for item in sublist if len(item) > 2]  # flatten
        compDefault = list(set(compDefault))        # make unique
        compFull = list(completions)
        compFull.extend(compDefault)
        compFull.sort()
        return (compFull, sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)