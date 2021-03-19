#coding=utf-8
import json
import os
import requests

SENDKEY = ""
USER = ""
BJOB_PATH = ""
LSF_ENVDIR = ""
LSF_BINDIR = ""
LSF_LIBDIR = ""
LSF_SERVERDIR = ""

os.chdir(os.path.dirname(os.path.abspath(__file__)))
fp = os.popen(
    "export LSF_ENVDIR=" + LSF_ENVDIR + ";" +
    "export LSF_BINDIR=" + LSF_BINDIR + ";" +
    "export LSF_LIBDIR=" + LSF_LIBDIR + ";" +
    "export LSF_SERVERDIR=" + LSF_SERVERDIR + ";" +
    BJOB_PATH + " -u " + USER + " 2>&1"
)
ret_str = fp.read()
fp.close()

job_id_dict = {}
job_ids = []
if not ret_str.startswith("No"):
    lines = ret_str.splitlines()
    start_index = lines[0].index("JOB_NAME")
    lines = lines[1:]
    for line in lines:
        if line.startswith(" "):
            continue
        job_id = int(line.split("   ")[0])
        job_name = line[start_index:]
        end_index = job_name.index(" ")
        job_name = job_name[:end_index]

        job_id_dict[str(job_id)] = job_name
        job_ids.append(job_id)

file_path = "data.json"
if not os.path.exists(file_path):
    fp = open(file_path, "w")
    fp.write("[{},[]]")
    fp.close()

fp = open(file_path, "r+")
old_job_id_dict, old_job_ids = json.load(fp)
fp.truncate(0)
fp.seek(0)
json.dump([job_id_dict, job_ids], fp)

finished_job_ids = list(set(old_job_ids) - (set(old_job_ids) & set(job_ids)))
if len(finished_job_ids) != 0:
    buf = []
    for _id in finished_job_ids:
        buf.append(str(_id) + "(" + (old_job_id_dict[str(_id)].encode("utf-8")) + ")")
    res = requests.post("https://sctapi.ftqq.com/" + SENDKEY + ".send", {
        "text": "超算计算通知",
        "desp": "任务" + (", ".join(buf)) + "完成了, 快去看看叭"
    }, headers={"content-type": "application/x-www-form-urlencoded"})