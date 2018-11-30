# -*- coding:utf-8 -*-
# import time
# from uiautomator import device as d
# print u'打开qq'
# d(text='QQ').click()
# d(text=u'登录').click()
# time.sleep(2)
# d(text=u'QQ号/手机号、邮箱').set.tsxt('1447127064')
# time.sleep(1)
# d(resourceId="com.tencent.mobileqq:id/password").set_text("weixiao123")
# d(resourceId="com.tencent.mobileqq:id/login").click()
# time.sleep(2)
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice
from com.android.monkeyrunner import MonkeyImage as mi
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By
from com.android.chimpchat.hierarchyviewer import HierarchyViewer
from com.android.hierarchyviewerlib.models import ViewNode

try:

    device = mr.waitForConnection()

except Exception:

    print 'device connect to VM failed!!!'

try:

    easyMonkey = EasyMonkeyDevice(device)

except Exception:

    print 'easyMonkey are not available!!!'

try:

    hierachy_view = device.getHierarchyViewer()

except Exception:

    print 'hierachy_view are not available!!!'


def returnhierarchyview():
    return device.getHierarchyViewer()


def returneasyMonkey():
    return EasyMonkeyDevice(device)


def returnfinviewbyid(idvalue):
    # hierachy_view=returnhierarchyview()

    return hierachy_view.findViewById(idvalue)


def returnById(idvalue):
    return By.id(idvalue)


def action_touch(widges, widgesname):
    easyMonkey = returneasyMonkey()

    print widgesname, 'is available?(True or Faulse)', easyMonkey.visible(widges)

    if (easyMonkey.visible(widges)):

        print 'the ---', widgesname, '----was touched'

        easyMonkey.touch(widges, MonkeyDevice.DOWN_AND_UP)

        mr.sleep(1)

    else:
        return 0


def action_type(widges, value):
    easyMonkey = returneasyMonkey()

    easyMonkey.type(widges, value)

    print 'if ', value, ' is available?(True or Faulse)  ', easyMonkey.visible(widges)

    print 'input a test case , value = ', value

    mr.sleep(1)


# test delivery man

# admname username

# password password

def testlogin(admname, password):
    mr.sleep(2)

    # easyMonkey=returneasyMonkey()

    # hierachy_view=returnhierarchyview()

    try:

        view_node1 = returnfinviewbyid('id/sidebar_fragment')

        view_node2 = returnfinviewbyid('id/ll_dispatcher')

        print('touch button delivery man')

        action1 = returnById("id/button_dispatcher")

        action_touch(action1, 'button dispatcher')

        view_node3 = returnfinviewbyid('id/content_fragment')

        view_node4 = returnfinviewbyid('id/account_num')

        adm = returnById("id/administrator_number")

        action_type(adm, admname)

        passw = returnById("id/password_edittext")

        action_type(passw, password)

        action4 = returnById("id/login")

        action_touch(action4, 'button login')

        print "sleep for 3 seconds!!"

        mr.sleep(3)

    except NameError:

        print 'the id can not be found!!!'


#########################################################

def getgoods():
    easyMonkey = returneasyMonkey()

    # hierachy_view=returnhierarchyview()

    layoutview01 = returnfinviewbyid('id/linearLayout_body_sreenSaver')

    view_node3 = returnfinviewbyid('id/content_fragment')

    layoutview01 = returnfinviewbyid('id/linearlayout_cabinet_2_10')

    if layoutview01 is None:

        layoutview01 = returnfinviewbyid('id/linearlayout_cabinet_4_10')

        layoutview02 = returnfinviewbyid('id/linearlayout_cabinet_opendoor_back2')

        button_back = returnById("id/cabinet_opendoor_back_410")

        action_touch(button_back, "cabinet_opendoor_back_410")

    else:

        linear_openback_view = returnfinviewbyid('id/linearlayout_cabinet_opendoor_back')

        button_back = returnById("id/cabinet_opendoor_back_210")

        action_touch(button_back, "cabinet_opendoor_back_210")


#########################################################

# test the function after login page.


def parceldelivery(order, phone):
    easyMonkey = returneasyMonkey()

    # hierachy_view=returnhierarchyview()

    # view_node = returnfinviewbyid('id/content_fragment')

    dilivePackage = returnById("id/dilivePackage")

    action_touch(dilivePackage, "dilivePackage")

    orderId = returnById("id/orderId")

    textstr = easyMonkey.getText(orderId)

    if (textstr == ''):

        action_type(orderId, order)

    else:

        empty1 = returnById("id/empty")

        action_touch(empty1, "empty")

        # easyMonkey.setText(orderId,"")

        action_type(orderId, order)

    phoneNum = returnById("id/phoneNum")

    text = easyMonkey.getText(phoneNum)

    if (text == ''):

        action_type(phoneNum, phone)


    else:

        # easyMonkey.setText(phoneNum,"")

        empty2 = returnById("id/empty")

        action_touch(empty2, "empty")

        action_type(phoneNum, phone)

    button_next = returnById("id/button_next")

    action_touch(button_next, "button_next")

    print "sleep for 6 seconds!!"

    mr.sleep(6)

    getgoods()


# button_diliv_back = returnById("id/button_diliv_back")

# action_touch(button_diliv_back,"button_diliv_back")


def takegoods(identifycode):
    sider_layou = returnfinviewbyid('linearLayout_side_sreenSaver')

    tackgood_layout = returnfinviewbyid('id/sidebar_fragment')

    ll_getpackage = returnfinviewbyid('ll_getpackage')

    action1 = returnById("id/button_getpackage")

    action_touch(action1, 'button getpachage')

    layoutview01 = returnfinviewbyid('id/linearLayout_body_sreenSaver')

    view_node3 = returnfinviewbyid('id/content_fragment')

    relativeview = returnfinviewbyid('charge_card_number1')

    edit_getpackage = returnById("id/take_goods_number")

    action_type(edit_getpackage, identifycode)

    take_goods_enter = returnById('id/take_goods_enter')

    action_touch(take_goods_enter, "take_goods_enter")

    print "sleep for 6 seconds!!"

    mr.sleep(6)

    getgoods()


##########################################################

if __name__ == '__main__':

    import codecs

    import time

    time_format = '%Y-%m-%d %X'

    try:

        codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

        print('APP start to test...')

        print('start robot main activity')

        componentName = '包名/.MainActivity'

        device.startActivity(component=componentName)

        print('MainActivity begin to run')

        mr.sleep(3)

    except Exception:

        print 'this is somehing wrong!!!'

    # test delivery activity

    # test case

    # testlogin('123456','000000')

    # testlogin('12345678','000000')

    # testlogin('123','000000')

    # test parcel delivery

    # test case

    # parceldelivery('1234564','15678909878')

    # parceldelivery('123456','156789098')

    # parceldelivery('1234','15678909878')

    # parceldelivery('','')

    # parceldelivery('','15678909878')

    # parceldelivery('123456','')

    try:

        for i in range(1, 10):
            print '<<<<<<<<<<<<<<<<<<<<<<<<<<', 'This is the   ', i, '  times to run>>>>>>>>>>'

            print 'the current time is  ', time.strftime(time_format, time.localtime())

            testlogin('300001', '987654')

            parceldelivery('1098000000001416801', '15983629282')

            takegoods('123456')

            print '\nthe end time is ', time.strftime(time_format, time.localtime())

            print '<<<<<<<<<<<<<<<<<<<<<<<<<<', 'the End of  ', i, '  times>>>>>>>>>>>\n\n'

    except Exception:

        print 'this is a exception occur...'


