Kod iz .csv file-a izvlači sve vrijednosti pomaka i vremena te onda dodaje još vremenskih koraka između postojećih te za njih linearnom aproksimacijom
računa nove vrijednosti pomaka za ta vremena. Broj vremenskih koraka može se mijenjati tako da se poveća ili smanji parametar N ili vrijeme kraja t_end.
- na mjestu u kodu gdje piše "test10.csv" treba napisati ime svojeg csv file-a.
- ako treba spremiti dobivene podatke u .csv file onda samo zadnju liniju u kodu treba maknuti iz komentara
- dio koji crta graf služi samo kao provjera da kod radi, plave točke s crvenim plusevima su postojeći podaci a točke bez pluseva su novi podaci
