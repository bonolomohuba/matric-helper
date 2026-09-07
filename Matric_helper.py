from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'some-random-secret-string'  # required for sessions to work securely

universities = [
    {
        'name': 'Wits',
        'aliases': ['university of the witwatersrand'],
        'aps': 34,
        'deadline': '30 September 2026',
        'prospectus_link': 'https://www.wits.ac.za/study-at-wits/undergraduate/'
    },
    {
        'name': 'UP',
        'aliases': ['university of pretoria', 'tuks'],
        'aps': 30,
        'deadline': '30 June 2026',
        'prospectus_link': 'https://www.up.ac.za/apply'
    },
    {
        'name': 'UJ',
        'aliases': ['university of johannesburg'],
        'aps': 24,
        'deadline': '31 October 2026',
        'prospectus_link': 'https://www.uj.ac.za/study-at-uj/apply/'
    },
    {
        'name': 'UCT',
        'aliases': ['university of cape town'],
        'aps': 34,
        'deadline': '31 July 2026',
        'prospectus_link': 'https://www.uct.ac.za/apply'
    },
    {
        'name': 'TUT',
        'aliases': ['tshwane university of technology'],
        'aps': 26,
        'deadline': '30 September 2026',
        'prospectus_link': 'https://www.tut.ac.za/prospective-students'
    },
    {
        'name': 'SMU',
        'aliases': ['sefako makgatho health sciences university'],
        'aps': 28,
        'deadline': '31 July 2026',
        'prospectus_link': 'https://www.smu.ac.za/'
    },
    {
        'name': 'Stellenbosch',
        'aliases': ['stellenbosch university', 'su', 'maties'],
        'aps': 32,
        'deadline': '31 July 2026',
        'prospectus_link': 'https://www.sun.ac.za/english/maties-choice/apply'
    },
    {
        'name': 'Rhodes',
        'aliases': ['rhodes university', 'ru'],
        'aps': 28,
        'deadline': '30 September 2026',
        'prospectus_link': 'https://www.ru.ac.za/prospectivestudents/'
    },
    {
        'name': 'NWU',
        'aliases': ['north-west university', 'north west university'],
        'aps': 24,
        'deadline': '30 August 2026',
        'prospectus_link': 'https://www.nwu.ac.za/how-to-apply'
    },
    {
        'name': 'UFS',
        'aliases': ['university of the free state', 'free state'],
        'aps': 24,
        'deadline': '30 September 2026',
        'prospectus_link': 'https://www.ufs.ac.za/apply'
    },
    {
        'name': 'UKZN',
        'aliases': ['university of kwazulu-natal', 'kwazulu natal'],
        'aps': 26,
        'deadline': '30 September 2026',
        'prospectus_link': 'https://www.ukzn.ac.za/apply/'
    },
    {
        'name': 'UWC',
        'aliases': ['university of the western cape', 'western cape'],
        'aps': 23,
        'deadline': '30 September 2026',
        'prospectus_link': 'https://www.uwc.ac.za/study/applications'
    },
    {
        'name': 'Fort Hare',
        'aliases': ['university of fort hare', 'ufh'],
        'aps': 22,
        'deadline': '31 October 2026',
        'prospectus_link': 'https://www.ufh.ac.za/apply'
    },
    {
        'name': 'Univen',
        'aliases': ['university of venda'],
        'aps': 22,
        'deadline': '30 September 2026',
        'prospectus_link': 'https://www.univen.ac.za/'
    },
    {
        'name': 'DUT',
        'aliases': ['durban university of technology'],
        'aps': 20,
        'deadline': '30 September 2026',
        'prospectus_link': 'https://www.dut.ac.za/apply/'
    },
    {
        'name': 'CPUT',
        'aliases': ['cape peninsula university of technology'],
        'aps': 20,
        'deadline': '30 September 2026',
        'prospectus_link': 'https://www.cput.ac.za/study/applications'
    },
    {
        'name': 'CUT',
        'aliases': ['central university of technology'],
        'aps': 20,
        'deadline': '30 September 2026',
        'prospectus_link': 'https://www.cut.ac.za/applications'
    },
    {
        'name': 'VUT',
        'aliases': ['vaal university of technology'],
        'aps': 20,
        'deadline': '30 September 2026',
        'prospectus_link': 'https://www.vut.ac.za/admissions/'
    },
    {
        'name': 'MUT',
        'aliases': ['mangosuthu university of technology'],
        'aps': 18,
        'deadline': '30 September 2026',
        'prospectus_link': 'https://www.mut.ac.za/'
    },
    {
        'name': 'UNISA',
        'aliases': ['university of south africa'],
        'aps': 18,
        'deadline': '1 January 2027',
        'prospectus_link': 'https://www.unisa.ac.za/sites/corporate/default/Apply-for-admission'
    },
    {
        'name': 'NMU',
        'aliases': ['nelson mandela university', 'nelson mandela'],
        'aps': 24,
        'deadline': '30 September 2026',
        'prospectus_link': 'https://www.mandela.ac.za/Study-at-Mandela/Applications'
    },
    {
        'name': 'UniZulu',
        'aliases': ['university of zululand', 'zululand'],
        'aps': 20,
        'deadline': '31 October 2026',
        'prospectus_link': 'https://www.unizulu.ac.za/'
    },
    {
        'name': 'WSU',
        'aliases': ['walter sisulu university'],
        'aps': 18,
        'deadline': '31 October 2026',
        'prospectus_link': 'https://www.wsu.ac.za/'
    },
    {
        'name': 'UL',
        'aliases': ['university of limpopo', 'limpopo'],
        'aps': 22,
        'deadline': '30 September 2026',
        'prospectus_link': 'https://www.ul.ac.za/'
    },
    {
        'name': 'SPU',
        'aliases': ['sol plaatje university'],
        'aps': 20,
        'deadline': '30 November 2026',
        'prospectus_link': 'https://www.spu.ac.za/'
    },
    {
        'name': 'UMP',
        'aliases': ['university of mpumalanga', 'mpumalanga'],
        'aps': 20,
        'deadline': '30 November 2026',
        'prospectus_link': 'https://www.ump.ac.za/'
    },
]



# MATERIALS DATA
materials = [
    {'subject': 'All Subjects - Past Exam Papers', 'source': 'Department of Basic Education', 'link': 'https://www.education.gov.za/Curriculum/NationalSeniorCertificate(NSC)Examinations/NSCPastExaminationpapers.aspx'},
    {'subject': 'Free Textbooks (Maths, Science & more)', 'source': 'Siyavula', 'link': 'https://www.siyavula.com/read'},
]

#here we wanna calculate the aps score of each student
def get_points(percentage):
    if percentage >= 80:
        return 7
    elif percentage >= 70:
        return 6
    elif percentage >= 60:
        return 5
    elif percentage >= 50:
        return 4
    elif percentage >= 40:
        return 3
    elif percentage >= 30:
        return 2
    else:
        return 1

@app.route('/')
def welcome():
    return render_template('welcome.html')   

@app.route('/home')
def home():
    return render_template('index.html', universities=universities)

@app.route('/search', methods=['GET', 'POST'])
def search():
    result = None
    if request.method == 'POST':
        searched_name = request.form['uni_name'].lower()
        for uni in universities:
            if uni['name'].lower() == searched_name or searched_name in uni['aliases']:
                result = uni
                break
    return render_template('search.html', result=result)

#ROUTE FOR APS CALCULATOR
@app.route('/aps-calculator', methods=['GET', 'POST'])
def aps_calculator():
    total_aps = None
    qualifying_universities = []
    error = None

    if request.method == 'POST':
        try:
            subject1 = float(request.form['subject1'])
            subject2 = float(request.form['subject2'])
            subject3 = float(request.form['subject3'])
            subject4 = float(request.form['subject4'])
            subject5 = float(request.form['subject5'])
            subject6 = float(request.form['subject6'])

            if any(mark < 0 or mark > 100 for mark in [subject1, subject2, subject3, subject4, subject5, subject6]):
                error = "Percentages must be between 0 and 100."
            else:
                total_aps = (get_points(subject1) + get_points(subject2) + get_points(subject3)
                             + get_points(subject4) + get_points(subject5) + get_points(subject6))

                for uni in universities:
                    if total_aps >= uni['aps']:
                        qualifying_universities.append(uni)

        except ValueError:
            error = "Please enter valid numbers for all six subjects."

    return render_template('aps_calculator.html', total_aps=total_aps, qualifying_universities=qualifying_universities, error=error)

#ROUTE FOR STUDENT MATERIALS
@app.route('/materials')
def materials_page():
    return render_template('materials.html', materials=materials)

#COMPARING BETWEEN TWO UNI
def find_university(name):
    for uni in universities:
        if uni['name'] == name:
            return uni
    return None



@app.route('/compare', methods=['GET', 'POST'])
def compare():
    uni1_data = None
    uni2_data = None
    error = None

    if request.method == 'POST':
        uni1_name = request.form['uni1']
        uni2_name = request.form['uni2']

        if uni1_name == uni2_name:
            error = "Please select two different universities to compare."
        else:
            uni1_data = find_university(uni1_name)
            uni2_data = find_university(uni2_name)

    return render_template('compare.html', universities=universities, uni1_data=uni1_data, uni2_data=uni2_data, error=error)


#session plus cookies for favorites
@app.route('/add-favorite/<uni_name>')
def add_favorite(uni_name):
    if 'favorites' not in session:
        session['favorites'] = []

    if uni_name not in session['favorites']:
        session['favorites'].append(uni_name)
        session.modified = True

    return redirect('/favorites')

#The favorite page itself
@app.route('/favorites')
def favorites():
    favorite_names = session.get('favorites', [])
    favorite_universities = [uni for uni in universities if uni['name'] in favorite_names]
    return render_template('favorites.html', favorite_universities=favorite_universities)

#help service(B Mohuba)
@app.route('/apply-service')
def apply_service():
    return render_template('apply_service.html')

if __name__ == '__main__':
    app.run(debug=True)