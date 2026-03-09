CREATE DATABASE	ai_analysis;
USE ai_analysis;

CREATE TABLE ai_master AS
SELECT a.ref_area AS country,
    a.OBS_VALUE AS aipi_score,
    d.OBS_VALUE AS digital_score,
    i.OBS_VALUE AS innovation_score,
    h.OBS_VALUE AS human_capital_score,
    r.OBS_VALUE AS regulation_score
FROM imf_aipi a
INNER JOIN imf_digital_infrastructure d
	ON a.REF_AREA = d.REF_AREA
INNER JOIN imf_innovation i
	ON a.REF_AREA = i.REF_AREA
INNER JOIN imf_human_capital h
	ON a.REF_AREA = h.REF_AREA
INNER JOIN imf_regulation r
	ON a.REF_AREA = r.REF_AREA




