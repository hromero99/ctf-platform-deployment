import docker

docker_image = "kali:vnc"

users_list = ['exam 1157', 'exam 1158', 'exam 1159', 'exam 1160', 'exam 1161', 'exam 1162', 'exam 1163', 'exam 1164', 'exam 1165', 'exam 1166', 'exam 1167', 'exam 1168', 'exam 1169', 'exam 1170', 'exam 1171', 'exam 1172', 'exam 1173', 'exam 1174', 'exam 1175', 'exam 1176', 'exam 1177', 'exam 1178', 'exam 1179', 'exam 1180', 'exam 1181', 'exam 1182', 'exam 1183', 'exam 1184', 'exam 1185', 'exam 1186', 'exam 1187', 'exam 1188', 'exam 1189', 'exam 1190', 'exam 1191', 'exam 1192', 'exam 1193', 'exam 1194', 'exam 1195', 'exam 1196', 'exam 1197', 'exam 1198', 'exam 1199', 'exam 1200', 'exam 1201', 'exam 1202', 'exam 1203', 'exam 1204', 'exam 1205', 'exam 1206', 'exam 1207', 'exam 1208', 'exam 1209', 'exam 1210', 'exam 1211', 'exam 1212', 'exam 1213', 'exam 1214', 'exam 1215']

docker_client = docker.from_env()

initial_port = 8080

for user in users_list:
    docker_client.containers.run(
        image = docker_image,
        name = '_'.join(user.split(" ")),
        ports = {
            "8080" : initial_port
        },
        detach= True
    )
