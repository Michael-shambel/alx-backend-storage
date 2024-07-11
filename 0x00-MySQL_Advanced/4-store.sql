-- sql scrip that create a trigger that decrease the quantity of
-- an item afrer adding a new oerder

DELIMITER $$
CREATE TRIGGER decrease_quantity 
AFTER INSERT ON orders FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END $$
DELIMITER ;
