SELECT noc FROM nocs ORDER BY noc ASC;
SELECT DISTINCT athlete_name FROM athletes, results WHERE athletes.id = results.athlete_id AND results.team_id = 91;
SELECT athlete_id, team_id, noc_id, sport_id, event_id, medal, games FROM results JOIN games ON results.games_id = games.id WHERE athlete_id = 71665 ORDER BY year;
SELECT noc,COUNT(medal) FROM results JOIN nocs ON results.noc_id = nocs.id WHERE medal = 'Gold' GROUP BY nocs.noc ORDER BY COUNT(MEDAL) DESC;
