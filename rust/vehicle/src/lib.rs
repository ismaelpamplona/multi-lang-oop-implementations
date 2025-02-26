pub struct Vehicle {
    pub make: String,
    pub model: String,
    pub year: u16,
}

impl Vehicle {
    pub fn new(make: &str, model: &str, year: u16) -> Self {
        Self {
            make: make.to_string(),
            model: model.to_string(),
            year,
        }
    }

    pub fn age(&self, current_year: u16) -> u16 {
        current_year - self.year
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_vehicle_creation() {
        let car = Vehicle::new("Toyota", "Corolla", 2020);
        assert_eq!(car.make, "Toyota");
        assert_eq!(car.model, "Corolla");
        assert_eq!(car.year, 2020);
    }

    #[test]
    fn test_vehicle_age() {
        let car = Vehicle::new("Ford", "Focus", 2018);
        assert_eq!(car.age(2024), 6);
    }
}
