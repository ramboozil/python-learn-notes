CN_mobile = [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 182, 183, 184, 187, 188, 147, 178, 1705]
CN_union = [130, 131, 132, 155, 156, 185, 186, 145, 176, 1709]
CN_telecom = [133, 153, 180, 181, 189, 177, 1700]


def phone_validation():
    phone = input('Please enter your phoneNum:')
    if len(phone) == 11:
        prefix = int(phone[0:3])
        if prefix in CN_mobile:
            print('operator : China Mobile')
            print('We have send verification code to your phone {}'.format(str(phone)))
        elif prefix in CN_union:
            print('operator : China Union')
            print('We have send verification code to your phone {}'.format(str(phone)))
        elif prefix in CN_telecom:
            print('operator : China Telecom')
            print('We have send verification code to your phone {}'.format(str(phone)))
        else:
            print('No such an operator!')
            phone_validation()
    else:
        print('Invalid length,Your phone Number should be 11 digits')
        phone_validation()


phone_validation()
