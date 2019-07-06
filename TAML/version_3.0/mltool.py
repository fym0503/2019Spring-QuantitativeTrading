from sklearn.ensemble import AdaBoostClassifier
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
clf1 = LogisticRegression(solver='lbfgs', multi_class='multinomial',random_state=1)
clf2 = RandomForestClassifier(n_estimators=50, random_state=1)
clf3 = GaussianNB()
#clf = VotingClassifier(estimators=[('lr', clf1), ('rf', clf2), ('gnb', clf3)], voting='hard')
method=[]
method.append(DecisionTreeClassifier())
method.append(MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1))
method.append(KNeighborsClassifier(n_neighbors=10))
method.append(AdaBoostClassifier(n_estimators=10000))
method.append(RandomForestClassifier(n_estimators=100))
method.append(GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,max_depth=1, random_state=0))
#method.append(elcf)
method.append(svm.SVC())
method.append(linear_model.LinearRegression())
method.append(linear_model.Ridge(alpha=0.5))
method.append(linear_model.Lasso(alpha=0.1))
method.append(linear_model.BayesianRidge())
method.append(linear_model.LogisticRegression())
method.append(svm.SVR())
