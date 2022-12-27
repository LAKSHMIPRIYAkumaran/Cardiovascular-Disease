from django.shortcuts import render
import pandas as pd
import pickle, os, random
# Finding Cardiovascular Disease:
def Cardiovascular_finder(request):
    if request.method == 'POST':
        if request.POST.get('Target_button'):
            age = request.POST.get('age')
            sex = request.POST.get('sex')
            cp = request.POST.get('cp')
            trestbps = request.POST.get('trestbps')
            chol = request.POST.get('chol')
            fbs = request.POST.get('fbs')
            restecg = request.POST.get('restecg')
            thalach = request.POST.get('thalach')
            exang = request.POST.get('exang')
            oldpeak = request.POST.get('oldpeak')
            slope = request.POST.get('slope')
            ca = request.POST.get('ca')
            thal = request.POST.get('thal')
            # print(name)

            results = Finder( age, sex, cp, trestbps, chol, fbs,restecg,thalach, exang, oldpeak, slope, ca, thal)
            print(results)
            results = str(results[0])
        else:
            print('No Cardiovascular Disease')

    else:
        results = None

    return render(request, 'Health_form.html', {'result': results})


def Finder(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal ):
    df = pd.DataFrame(columns=[ 'age','sex', 'cp','trestbps', 'chol', 'fbs', 'restecg','thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'])
    df2= {'age': age, 'sex': sex, 'cp': cp, 'trestbps': trestbps, 'chol': chol, 'fbs': fbs, 'restecg':restecg, 'thalach':thalach, 'exang':exang, 'oldpeak': oldpeak, 'slope':slope, 'ca':ca, 'thal':thal}
    df = df.append(df2, ignore_index=True)

    # load the model from disk
    filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), r'heart\Finalized_model_RF.pickle')
    loaded_model = pickle.load(open(filename, 'rb'))
    res = loaded_model.predict(df)
    print(res)
    return res




