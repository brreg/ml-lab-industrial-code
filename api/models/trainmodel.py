# # This is a sample model to demonstrate how a Machine Learning model
# # can be implemented in Production as a REST API and how it can be consumed
#
# # Import libraries and packages
# from sklearn import svm, datasets
# from sklearn.externals import joblib
#
# # Load Sample data
# iris = datasets.load_iris()
#
# # Split loaded data into independent and target features
# X = iris.data
# y = iris.target
#
# # Train Support Vector Machine (SVM) model with all data
# svmModel = svm.SVC(kernel='poly', degree=3, C=1.0).fit(X, y)
#
# # Persist model so that it can be used by different consumers
# svmFile = open('SVMModel.pckl', 'wb')
# joblib.dump(svmModel, svmFile)
# svmFile.close()
