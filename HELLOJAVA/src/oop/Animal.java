package oop;

public class Animal {
	public boolean egg = false;
//	public int age = 0;
	private int age = 0;
	
	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	public void getOld() {
		age++;
	}
	public void changeEgg() {
		egg = !egg;
	}
}
