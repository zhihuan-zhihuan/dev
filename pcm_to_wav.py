import wave
import os


def file_gothrough(path, suffix):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file[-3:] == suffix:
                file_list.append(os.path.join(root, file))
    return file_list


def pcm2wav(pcm_path):
    f1 = file_gothrough(pcm_path, 'pcm')
    for pcmname in f1:
        pcmfile = open(pcmname, 'rb')
        pcmdata = pcmfile.read()
        with wave.open(pcmname[:-4] + '.wav', 'wb') as wavfile:
            wavfile.setparams((1, 2, 16000, 0, 'NONE', 'NONE'))
            wavfile.writeframes(pcmdata)



pcm2wav(r'pcm文件路径')