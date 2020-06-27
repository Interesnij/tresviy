from managers.models import AudioUserStaff, CanWorkStaffAudioUser
from logs.model.audio import AudioWorkerManageLog, AudioCreateWorkerManageLog


def add_audio_administrator(user, request_user):
    try:
        user.audio_user_staff.level = "A"
        user.audio_user_staff.save(update_fields=['level'])
    except:
        user_staff = AudioStaff.objects.create(user=user, level="A")
    AudioWorkerManageLog.objects.create(user=user, manager=request_user, action_type=CREATE_ADMIN)
    return user_staff

def add_audio_moderator(user, request_user):
    try:
        user.audio_user_staff.level = "M"
        user.audio_user_staff.save(update_fields=['level'])
    except:
        user_staff = AudioStaff.objects.create(user=user, level="M")
    AudioWorkerManageLog.objects.create(user=user, manager=request_user, action_type=CREATE_MODERATOR)
    return user_staff

def add_audio_editor(user, request_user):
    try:
        user.audio_user_staff.level = "E"
        user.audio_user_staff.save(update_fields=['level'])
    except:
        user_staff = AudioStaff.objects.create(user=user, level="E")
    AudioWorkerManageLog.objects.create(user=user, manager=request_user, action_type=CREATE_EDITOR)
    return user_staff

def remove_audio_administrator(user, request_user):
    try:
        user.audio_user_staff.level = ""
        user.audio_user_staff.save(update_fields=['level'])
        AudioWorkerManageLog.objects.create(user=user, manager=request_user, action_type=DELETE_ADMIN)
    except:
        pass

def remove_audio_moderator(user, request_user):
    try:
        user.audio_user_staff.level = ""
        user.audio_user_staff.save(update_fields=['level'])
        AudioWorkerManageLog.objects.create(user=user, manager=request_user, action_type=DELETE_MODERATOR)
    except:
        pass

def remove_audio_editor(user, request_user):
    try:
        user.audio_user_staff.level = ""
        user.audio_user_staff.save(update_fields=['level'])
        AudioWorkerManageLog.objects.create(user=user, manager=request_user, action_type=DELETE_EDITOR)
    except:
        pass


def add_audio_administrator_worker(user, request_user):
    try:
        user.can_work_staff_audio_user.is_administrator = True
        user.can_work_staff_audio_user.save(update_fields=['is_administrator'])
    except:
        user_staff = CanWorkStaffAudio.objects.create(user=user, is_administrator=True)
    AudioCreateWorkerManageLog.objects.create(user=user, manager=request_user, action_type=CREATE_ADMIN)
    return user_staff

def add_audio_moderator_worker(user, request_user):
    try:
        user.can_work_staff_audio_user.is_moderator = True
        user.can_work_staff_audio_user.save(update_fields=['is_moderator'])
    except:
        user_staff = CanWorkStaffAudio.objects.create(user=user, is_moderator=True)
    AudioCreateWorkerManageLog.objects.create(user=user, manager=request_user, action_type=CREATE_MODERATOR)
    return user_staff

def add_audio_editor_worker(user, request_user):
    try:
        user.can_work_staff_audio_user.is_editor = True
        user.can_work_staff_audio_user.save(update_fields=['is_editor'])
    except:
        user_staff = CanWorkStaffAudio.objects.create(user=user, is_editor=True)
    AudioCreateWorkerManageLog.objects.create(user=user, manager=request_user, action_type=CREATE_ADVERTISER)
    return user_staff

def remove_audio_administrator_worker(user, request_user):
    try:
        user.can_work_staff_audio_user.is_administrator = False
        user.can_work_staff_audio_user.save(update_fields=['is_administrator'])
        AudioCreateWorkerManageLog.objects.create(user=user, manager=request_user, action_type=DELETE_ADMIN)
    except:
        pass

def remove_audio_moderator_worker(user, request_user):
    try:
        user.can_work_staff_audio_user.is_moderator = False
        user.can_work_staff_audio_user.save(update_fields=['is_moderator'])
        AudioCreateWorkerManageLog.objects.create(user=user, manager=request_user, action_type=DELETE_MODERATOR)
    except:
        pass

def remove_audio_editor_worker(user, request_user):
    try:
        user.can_work_staff_audio_user.is_editor = False
        user.can_work_staff_audio_user.save(update_fields=['is_editor'])
        AudioCreateWorkerManageLog.objects.create(user=user, manager=request_user, action_type=DELETE_EDITOR)
    except:
        pass