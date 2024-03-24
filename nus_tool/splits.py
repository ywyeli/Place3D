# nuScenes dev-kit.
# Code written by Holger Caesar, 2018.

from typing import Dict, List

from nuscenes import NuScenes

train_detect = \
    ['carla-1001', 'carla-1002', 'carla-1003', 'carla-1004', 'carla-1005', 'carla-1006', 'carla-1007', 'carla-1008',
     'carla-1009', 'carla-1010', 'carla-1011', 'carla-1012', 'carla-1013', 'carla-1014', 'carla-1015', 'carla-1016',
     'carla-1017', 'carla-1018', 'carla-1019', 'carla-1020', 'carla-1021', 'carla-1022', 'carla-1023', 'carla-1024',
     'carla-1025', 'carla-1026', 'carla-1027', 'carla-1028', 'carla-1029', 'carla-1030', 'carla-1031', 'carla-1032',
     'carla-1033', 'carla-1034', 'carla-1035', 'carla-1036', 'carla-1037', 'carla-1038', 'carla-1039', 'carla-1040',
     'carla-1041', 'carla-1042', 'carla-1043', 'carla-1044', 'carla-1045', 'carla-1046', 'carla-1047', 'carla-1048',
     'carla-1049', 'carla-1050', 'carla-1051', 'carla-1052', 'carla-1053', 'carla-1054', 'carla-1055', 'carla-1056',
     'carla-1057', 'carla-1058', 'carla-1059', 'carla-1060', 'carla-1061', 'carla-1062', 'carla-1063', 'carla-1064',
     'carla-1065', 'carla-1066', 'carla-1067', 'carla-1068', 'carla-1069', 'carla-1070', 'carla-1071', 'carla-1072',
     'carla-1073', 'carla-1074', 'carla-1075', 'carla-1076', 'carla-1077', 'carla-1078', 'carla-1079', 'carla-1080',
     'carla-1081', 'carla-1082', 'carla-1083', 'carla-1084', 'carla-1085', 'carla-1086', 'carla-1087', 'carla-1088',
     'carla-1089', 'carla-1090', 'carla-1091', 'carla-1092', 'carla-1093', 'carla-1094', 'carla-1095', 'carla-1096',
     'carla-1097', 'carla-1098', 'carla-1099', 'carla-1100', 'carla-1101', 'carla-1102', 'carla-1103', 'carla-1104',
     'carla-1105', 'carla-1106', 'carla-1107', 'carla-1108', 'carla-1109', 'carla-1110', 'carla-1111', 'carla-1112',
     'carla-1113', 'carla-1114', 'carla-1115', 'carla-1116', 'carla-1117', 'carla-1118', 'carla-1119', 'carla-1120',
     'carla-1121', 'carla-1122', 'carla-1123', 'carla-1124', 'carla-1125', 'carla-1126', 'carla-1127', 'carla-1128',
     'carla-1129', 'carla-1130', 'carla-1131', 'carla-1132', 'carla-1133', 'carla-1134', 'carla-1135', 'carla-1136',
     'carla-1137', 'carla-1138', 'carla-1139', 'carla-1140', 'carla-1141', 'carla-1142', 'carla-1143', 'carla-1144',
     'carla-1145', 'carla-1146', 'carla-1147', 'carla-1148', 'carla-1149', 'carla-1150', 'carla-1151', 'carla-1152',
     'carla-1153', 'carla-1154', 'carla-1155', 'carla-1156', 'carla-1157', 'carla-1158', 'carla-1159', 'carla-1160',
     'carla-1161', 'carla-1162', 'carla-1163', 'carla-1164', 'carla-1165', 'carla-1166', 'carla-1167', 'carla-1168',
     'carla-1169', 'carla-1170', 'carla-1171', 'carla-1172', 'carla-1173', 'carla-1174', 'carla-1175', 'carla-1176',
     'carla-1177', 'carla-1178', 'carla-1179', 'carla-1180', 'carla-1181', 'carla-1182', 'carla-1183', 'carla-1184',
     'carla-1185', 'carla-1186', 'carla-1187', 'carla-1188', 'carla-1189', 'carla-1190', 'carla-1191', 'carla-1192',
     'carla-1193', 'carla-1194', 'carla-1195', 'carla-1196', 'carla-1197', 'carla-1198', 'carla-1199', 'carla-1200',
     'carla-1201', 'carla-1202', 'carla-1203', 'carla-1204', 'carla-1205', 'carla-1206', 'carla-1207', 'carla-1208',
     'carla-1209', 'carla-1210', 'carla-1211', 'carla-1212', 'carla-1213', 'carla-1214', 'carla-1215', 'carla-1216',
     'carla-1217', 'carla-1218', 'carla-1219', 'carla-1220', 'carla-1221', 'carla-1222', 'carla-1223', 'carla-1224',
     'carla-1225', 'carla-1226', 'carla-1227', 'carla-1228', 'carla-1229', 'carla-1230', 'carla-1231', 'carla-1232',
     'carla-1233', 'carla-1234', 'carla-1235', 'carla-1236', 'carla-1237', 'carla-1238', 'carla-1239', 'carla-1240',
     'carla-1241', 'carla-1242', 'carla-1243', 'carla-1244', 'carla-1245', 'carla-1246', 'carla-1247', 'carla-1248',
     'carla-1249', 'carla-1250', 'carla-1251', 'carla-1252', 'carla-1253', 'carla-1254', 'carla-1255', 'carla-1256',
     'carla-1257', 'carla-1258', 'carla-1259', 'carla-1260', 'carla-1261', 'carla-1262', 'carla-1263', 'carla-1264',
     'carla-1265', 'carla-1266', 'carla-1267', 'carla-1268', 'carla-1269', 'carla-1270', 'carla-1271', 'carla-1272',
     'carla-1273', 'carla-1274', 'carla-1275', 'carla-1276', 'carla-1277', 'carla-1278', 'carla-1279', 'carla-1280']

train_track = \
    ['scene-0004', 'scene-0005', 'scene-0006', 'scene-0007', 'scene-0008', 'scene-0009', 'scene-0010', 'scene-0011',
     'scene-0019', 'scene-0020', 'scene-0021', 'scene-0022', 'scene-0023', 'scene-0024', 'scene-0025', 'scene-0026',
     'scene-0027', 'scene-0028', 'scene-0029', 'scene-0030', 'scene-0031', 'scene-0032', 'scene-0033', 'scene-0034',
     'scene-0120', 'scene-0121', 'scene-0122', 'scene-0123', 'scene-0124', 'scene-0125', 'scene-0126', 'scene-0127',
     'scene-0128', 'scene-0129', 'scene-0130', 'scene-0131', 'scene-0132', 'scene-0133', 'scene-0134', 'scene-0135',
     'scene-0138', 'scene-0139', 'scene-0149', 'scene-0150', 'scene-0151', 'scene-0152', 'scene-0154', 'scene-0155',
     'scene-0157', 'scene-0158', 'scene-0159', 'scene-0160', 'scene-0177', 'scene-0178', 'scene-0179', 'scene-0180',
     'scene-0181', 'scene-0182', 'scene-0183', 'scene-0184', 'scene-0185', 'scene-0187', 'scene-0188', 'scene-0218',
     'scene-0219', 'scene-0220', 'scene-0222', 'scene-0224', 'scene-0225', 'scene-0226', 'scene-0227', 'scene-0228',
     'scene-0229', 'scene-0230', 'scene-0231', 'scene-0232', 'scene-0233', 'scene-0234', 'scene-0235', 'scene-0236',
     'scene-0237', 'scene-0238', 'scene-0239', 'scene-0240', 'scene-0241', 'scene-0242', 'scene-0243', 'scene-0244',
     'scene-0245', 'scene-0246', 'scene-0247', 'scene-0248', 'scene-0249', 'scene-0250', 'scene-0251', 'scene-0252',
     'scene-0253', 'scene-0328', 'scene-0376', 'scene-0377', 'scene-0378', 'scene-0379', 'scene-0380', 'scene-0381',
     'scene-0383', 'scene-0384', 'scene-0385', 'scene-0386', 'scene-0388', 'scene-0389', 'scene-0390', 'scene-0391',
     'scene-0392', 'scene-0393', 'scene-0394', 'scene-0395', 'scene-0396', 'scene-0397', 'scene-0398', 'scene-0399',
     'scene-0400', 'scene-0401', 'scene-0402', 'scene-0403', 'scene-0405', 'scene-0406', 'scene-0407', 'scene-0408',
     'scene-0410', 'scene-0411', 'scene-0412', 'scene-0413', 'scene-0414', 'scene-0415', 'scene-0416', 'scene-0417',
     'scene-0418', 'scene-0419', 'scene-0440', 'scene-0441', 'scene-0442', 'scene-0443', 'scene-0444', 'scene-0445',
     'scene-0446', 'scene-0447', 'scene-0448', 'scene-0449', 'scene-0450', 'scene-0451', 'scene-0452', 'scene-0453',
     'scene-0454', 'scene-0455', 'scene-0456', 'scene-0499', 'scene-0500', 'scene-0501', 'scene-0502', 'scene-0504',
     'scene-0505', 'scene-0506', 'scene-0507', 'scene-0508', 'scene-0509', 'scene-0510', 'scene-0511', 'scene-0512',
     'scene-0513', 'scene-0514', 'scene-0515', 'scene-0517', 'scene-0518', 'scene-0525', 'scene-0526', 'scene-0527',
     'scene-0528', 'scene-0529', 'scene-0530', 'scene-0531', 'scene-0532', 'scene-0533', 'scene-0534', 'scene-0535',
     'scene-0536', 'scene-0537', 'scene-0538', 'scene-0539', 'scene-0541', 'scene-0542', 'scene-0543', 'scene-0544',
     'scene-0545', 'scene-0546', 'scene-0584', 'scene-0585', 'scene-0586', 'scene-0587', 'scene-0588', 'scene-0589',
     'scene-0590', 'scene-0591', 'scene-0592', 'scene-0593', 'scene-0594', 'scene-0595', 'scene-0596', 'scene-0597',
     'scene-0598', 'scene-0599', 'scene-0600', 'scene-0639', 'scene-0640', 'scene-0641', 'scene-0642', 'scene-0643',
     'scene-0644', 'scene-0645', 'scene-0646', 'scene-0647', 'scene-0648', 'scene-0649', 'scene-0650', 'scene-0651',
     'scene-0652', 'scene-0653', 'scene-0654', 'scene-0655', 'scene-0656', 'scene-0657', 'scene-0658', 'scene-0659',
     'scene-0660', 'scene-0661', 'scene-0662', 'scene-0663', 'scene-0664', 'scene-0695', 'scene-0696', 'scene-0697',
     'scene-0698', 'scene-0700', 'scene-0701', 'scene-0703', 'scene-0704', 'scene-0705', 'scene-0706', 'scene-0707',
     'scene-0708', 'scene-0709', 'scene-0710', 'scene-0711', 'scene-0712', 'scene-0713', 'scene-0714', 'scene-0715',
     'scene-0716', 'scene-0717', 'scene-0718', 'scene-0719', 'scene-0726', 'scene-0727', 'scene-0728', 'scene-0730',
     'scene-0731', 'scene-0733', 'scene-0734', 'scene-0735', 'scene-0736', 'scene-0737', 'scene-0738', 'scene-0786',
     'scene-0787', 'scene-0789', 'scene-0790', 'scene-0791', 'scene-0792', 'scene-0803', 'scene-0804', 'scene-0805',
     'scene-0806', 'scene-0808', 'scene-0809', 'scene-0810', 'scene-0811', 'scene-0812', 'scene-0813', 'scene-0815',
     'scene-0816', 'scene-0817', 'scene-0819', 'scene-0820', 'scene-0821', 'scene-0822', 'scene-0847', 'scene-0848',
     'scene-0849', 'scene-0850', 'scene-0851', 'scene-0852', 'scene-0853', 'scene-0854', 'scene-0855', 'scene-0856',
     'scene-0858', 'scene-0860', 'scene-0861', 'scene-0862', 'scene-0863', 'scene-0864', 'scene-0865', 'scene-0866',
     'scene-0992', 'scene-0994', 'scene-0995', 'scene-0996', 'scene-0997', 'scene-0998', 'scene-0999', 'scene-1000',
     'scene-1001', 'scene-1002', 'scene-1003', 'scene-1004', 'scene-1005', 'scene-1006', 'scene-1007', 'scene-1008',
     'scene-1009', 'scene-1010', 'scene-1044', 'scene-1045', 'scene-1046', 'scene-1047', 'scene-1048', 'scene-1049',
     'scene-1050', 'scene-1051', 'scene-1052', 'scene-1053', 'scene-1054', 'scene-1055', 'scene-1056', 'scene-1057',
     'scene-1058', 'scene-1106', 'scene-1107', 'scene-1108', 'scene-1109', 'scene-1110']

train = list(sorted(set(train_detect + train_track)))

val = \
    ['carla-1281', 'carla-1282', 'carla-1283', 'carla-1284', 'carla-1285', 'carla-1286', 'carla-1287', 'carla-1288',
     'carla-1289', 'carla-1290', 'carla-1291', 'carla-1292', 'carla-1293', 'carla-1294', 'carla-1295', 'carla-1296',
     'carla-1297', 'carla-1298', 'carla-1299', 'carla-1300', 'carla-1301', 'carla-1302', 'carla-1303', 'carla-1304',
     'carla-1305', 'carla-1306', 'carla-1307', 'carla-1308', 'carla-1309', 'carla-1310', 'carla-1311', 'carla-1312',
     'carla-1313', 'carla-1314', 'carla-1315', 'carla-1316', 'carla-1317', 'carla-1318', 'carla-1319', 'carla-1320',
     'carla-1321', 'carla-1322', 'carla-1323', 'carla-1324', 'carla-1325', 'carla-1326', 'carla-1327', 'carla-1328',
     'carla-1329', 'carla-1330', 'carla-1331', 'carla-1332', 'carla-1333', 'carla-1334', 'carla-1335', 'carla-1336',
     'carla-1337', 'carla-1338', 'carla-1339', 'carla-1340']

test = \
    []

mini_train = \
    []

mini_val = \
    []


def create_splits_logs(split: str, nusc: 'NuScenes') -> List[str]:
    """
    Returns the logs in each dataset split of nuScenes.
    Note: Previously this script included the teaser dataset splits. Since new scenes from those logs were added and
          others removed in the full dataset, that code is incompatible and was removed.
    :param split: NuScenes split.
    :param nusc: NuScenes instance.
    :return: A list of logs in that split.
    """
    # Load splits on a scene-level.
    scene_splits = create_splits_scenes(verbose=False)

    assert split in scene_splits.keys(), 'Requested split {} which is not a known nuScenes split.'.format(split)

    # Check compatibility of split with nusc_version.
    version = nusc.version
    if split in {'train', 'val', 'train_detect', 'train_track'}:
        assert version.endswith('trainval'), \
            'Requested split {} which is not compatible with NuScenes version {}'.format(split, version)
    elif split in {'mini_train', 'mini_val'}:
        assert version.endswith('mini'), \
            'Requested split {} which is not compatible with NuScenes version {}'.format(split, version)
    elif split == 'test':
        assert version.endswith('test'), \
            'Requested split {} which is not compatible with NuScenes version {}'.format(split, version)
    else:
        raise ValueError('Requested split {} which this function cannot map to logs.'.format(split))

    # Get logs for this split.
    scene_to_log = {scene['name']: nusc.get('log', scene['log_token'])['logfile'] for scene in nusc.scene}
    logs = set()
    scenes = scene_splits[split]
    for scene in scenes:
        logs.add(scene_to_log[scene])

    return list(logs)


def create_splits_scenes(verbose: bool = False) -> Dict[str, List[str]]:
    """
    Similar to create_splits_logs, but returns a mapping from split to scene names, rather than log names.
    The splits are as follows:
    - train/val/test: The standard splits of the nuScenes dataset (700/150/150 scenes).
    - mini_train/mini_val: Train and val splits of the mini subset used for visualization and debugging (8/2 scenes).
    - train_detect/train_track: Two halves of the train split used for separating the training sets of detector and
        tracker if required.
    :param verbose: Whether to print out statistics on a scene level.
    :return: A mapping from split name to a list of scenes names in that split.
    """
    # Use hard-coded splits.
    all_scenes = train + val + test
    # assert len(all_scenes) == 1000 and len(set(all_scenes)) == 1000, 'Error: Splits incomplete!'
    scene_splits = {'train': train, 'val': val, 'test': test,
                    'mini_train': mini_train, 'mini_val': mini_val,
                    'train_detect': train_detect, 'train_track': train_track}

    # Optional: Print scene-level stats.
    if verbose:
        for split, scenes in scene_splits.items():
            print('%s: %d' % (split, len(scenes)))
            print('%s' % scenes)

    return scene_splits


if __name__ == '__main__':
    # Print the scene-level stats.
    create_splits_scenes(verbose=True)
