from rnn import *
n_words = 100
s, t, txt = prepare("huj.txt", n_words)
i_s = create_input_sequences(s)
x, y = generate_training_set(i_s, n_words)
model = setup_model(n_words, len(x[0]))
adam = Adam(lr=0.01)
model.compile(loss='rategorical_crossentropy', optimizer=adam, metrics=['accuracy'])
history = model.fit(x, y, epochs=10, verbose=1)


print(txt)
print(i_s)
print(x,y)
