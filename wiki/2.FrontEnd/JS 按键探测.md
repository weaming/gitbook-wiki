## 戳这里：[传送门](/demo/key-check/)

注意事项：

- onkeypress事件的keyCode无法区分主键盘数字键和小键盘数字键
- 三个事件的执行顺序如下：onkeydown -> onkeypress ->onkeyup
- 把 document.returnValue 设为 false，可屏蔽浏览器对它的捕获。

JS代码如下：

```
$("html").keydown(function(e) {
    $("#keyDown").text(e.keyCode);
    var keyName;
    switch(e.keyCode)
    {
        case 8:keyName = "[退格]";break;
        case 9:keyName = "[Tab]";break;
        case 12:keyName = "[Clear]";break;
        case 13:keyName = "[Enter]";break;
        case 16:keyName = "[Shift]";break;
        case 17:keyName = "[Ctrl]";break;
        case 18:keyName = "[Alt]";break;
        case 19:keyName = "[PauseBreak]";break;
        case 20:keyName = "[Caps Lock]";break;
        case 27:keyName = "[Esc]";break;
        case 32:keyName = "[空格]";break;
        case 33:keyName = "[PageUp]";break;
        case 34:keyName = "[PageDown]";break;
        case 35:keyName = "[End]";break;
        case 36:keyName = "[Home]";break;
        case 37:keyName = "[方向键左]";break;
        case 38:keyName = "[方向键上]";break;
        case 39:keyName = "[方向键右]";break;
        case 40:keyName = "[方向键下]";break;
        case 41:keyName = "[Select]";break;
        case 42:keyName = "[Print]";break;
        case 43:keyName = "[Execute]";break;
        case 45:keyName = "[Insert]";break;
        case 46:keyName = "[Delete]";break;
        case 47:keyName = "[Help]";break;
        case 48:keyName = "[主键盘 0]";break;
        case 49:keyName = "[主键盘 1]";break;
        case 50:keyName = "[主键盘 2]";break;
        case 51:keyName = "[主键盘 3]";break;
        case 52:keyName = "[主键盘 4]";break;
        case 53:keyName = "[主键盘 5]";break;
        case 54:keyName = "[主键盘 6]";break;
        case 55:keyName = "[主键盘 7]";break;
        case 56:keyName = "[主键盘 8]";break;
        case 57:keyName = "[主键盘 9]";break;
        case 65:keyName = "[a A]";break;
        case 66:keyName = "[b B]";break;
        case 67:keyName = "[c C]";break;
        case 68:keyName = "[d D]";break;
        case 69:keyName = "[e E]";break;
        case 70:keyName = "[f F]";break;
        case 71:keyName = "[g G]";break;
        case 72:keyName = "[h H]";break;
        case 73:keyName = "[i I]";break;
        case 74:keyName = "[j J]";break;
        case 75:keyName = "[k K]";break;
        case 76:keyName = "[l L]";break;
        case 77:keyName = "[m M]";break;
        case 78:keyName = "[n N]";break;
        case 79:keyName = "[o O]";break;
        case 80:keyName = "[p P]";break;
        case 81:keyName = "[q Q]";break;
        case 82:keyName = "[r R]";break;
        case 83:keyName = "[s S]";break;
        case 84:keyName = "[t T]";break;
        case 85:keyName = "[u U]";break;
        case 86:keyName = "[v V]";break;
        case 87:keyName = "[w W]";break;
        case 88:keyName = "[x X]";break;
        case 89:keyName = "[y Y]";break;
        case 90:keyName = "[z Z]";break;
        case 91:keyName = "[左Win]";break;
        case 92:keyName = "[右Win]";break;
        case 93:keyName = "[快捷菜单键]";break;
        case 95:keyName = "[Sleep]";break;
        case 96:keyName = "[小键盘区0]";break;
        case 97:keyName = "[小键盘区1]";break;
        case 98:keyName = "[小键盘区2]";break;
        case 99:keyName = "[小键盘区3]";break;
        case 100:keyName = "[小键盘区4]";break;
        case 101:keyName = "[小键盘区5]";break;
        case 102:keyName = "[小键盘区6]";break;
        case 103:keyName = "[小键盘区7]";break;
        case 104:keyName = "[小键盘区8]";break;
        case 105:keyName = "[小键盘区9]";break;
        case 106:keyName = "[*]";break;
        case 107:keyName = "[+]";break;
        case 109:keyName = "[-]";break;
        case 110:keyName = "[.]";break;
        case 111:keyName = "[/]";break;
        case 112:keyName = "[F1]";break;
        case 113:keyName = "[F2]";break;
        case 114:keyName = "[F3]";break;
        case 115:keyName = "[F4]";break;
        case 116:keyName = "[F5]";break;
        case 117:keyName = "[F6]";break;
        case 118:keyName = "[F7]";break;
        case 119:keyName = "[F8]";break;
        case 120:keyName = "[F9]";break;
        case 121:keyName = "[F10]";break;
        case 122:keyName = "[F11]";break;
        case 123:keyName = "[F12]";break;
        case 124:keyName = "[F13]";break;
        case 125:keyName = "[F14]";break;
        case 126:keyName = "[F15]";break;
        case 127:keyName = "[F16]";break;
        case 128:keyName = "[F17]";break;
        case 129:keyName = "[F18]";break;
        case 130:keyName = "[F19]";break;
        case 131:keyName = "[F20]";break;
        case 132:keyName = "[F21]";break;
        case 133:keyName = "[F22]";break;
        case 134:keyName = "[F23]";break;
        case 135:keyName = "[F24]";break;
        case 136:keyName = "[Num_Lock]";break;
        case 137:keyName = "[Scroll_Lock]";break;
        case 144:keyName = "[NumLock]";break;
        case 145:keyName = "[ScrollLock]";break;
        case 186:keyName = "[;]";break;
        case 187:keyName = "[=]";break;
        case 188:keyName = "[,]";break;
        case 189:keyName = "[-]";break;
        case 190:keyName = "[.]";break;
        case 191:keyName = "[/]";break;
        case 192:keyName = "[`]";break;
        case 210:keyName = "[plusminus hyphen macron]";break;
        case 211:keyName = "[]";break;
        case 212:keyName = "[copyright registered]";break;
        case 213:keyName = "[guillemotleft guillemotright]";break;
        case 214:keyName = "[masculine ordfeminine]";break;
        case 215:keyName = "[ae AE]";break;
        case 216:keyName = "[cent yen]";break;
        case 217:keyName = "[questiondown exclamdown]";break;
        case 218:keyName = "[onequarter onehalf threequarters]";break;
        case 219:keyName = "[[]";break;
        case 220:keyName = "[//]";break;
        case 221:keyName = "[]]";break;
        case 222:keyName = "[']";break;
        default:keyName = "[" + String.fromCharCode(e.keyCode) + "]";break;
    }
    $("#keyName").text(keyName);
    event.returnValue = false;
})
```