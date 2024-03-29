SELECT C.APNT_NO, A.PT_NAME, C.PT_NO, C.MCDP_CD, B.DR_NAME, C.APNT_YMD
FROM PATIENT AS A JOIN DOCTOR AS B JOIN APPOINTMENT AS C
ON A.PT_NO = C.PT_NO AND B.DR_ID = C.MDDR_ID
WHERE C.MCDP_CD = 'CS' AND APNT_CNCL_YN = 'N' AND APNT_YMD LIKE '2022-04-13%'
ORDER BY APNT_YMD;